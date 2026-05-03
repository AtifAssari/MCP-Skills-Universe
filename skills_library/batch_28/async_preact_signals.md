---
title: async-preact-signals
url: https://skills.sh/rodydavis/skills/async-preact-signals
---

# async-preact-signals

skills/rodydavis/skills/async-preact-signals
async-preact-signals
Installation
$ npx skills add https://github.com/rodydavis/skills --skill async-preact-signals
SKILL.md
Async Preact Signals

When working with signals in Javascript, it is very common to work with async data from Promises.

Async vs Sync

But unlike other state management libraries, signals do not have an asynchronous state graph and all values must be computed synchronously.

When people first start using signals they want to simply add async to the function callback but this breaks how they work under the hood and leads to undefined behavior. ☹️

Async functions are a leaky abstraction and force you to handle them all the way up the graph. Async is also not always better and can have a performance impact. 😬

Working with Promises

We can still do so much with sync operations, and make it eaiser to work with common async patterns.

For example when you make a http request using fetch, you want to return the data in the Promise and update some UI.

const el = document.querySelector('#output');
let postId = '123';
fetch(`/posts/${postId}`).then(res => res.json()).then(post => {
    el.innerText = post.title;
})


Now when we add signals we can rerun the fetch everytime the post id changes.

import { effect, signal } from "@preact/signals-core";

const el = document.querySelector('#output');
const postId =  signal( '123');

effect(() => {
    fetch(`/posts/${postId.value}`).then(res => res.json()).then(post => {
        el.innerText = post.title;
    });
});


This is better, but now we need to handle stopping the previous request if the post id changes before the previous fetch completes.

import { effect, signal } from "@preact/signals-core";

const el = document.querySelector('#output');
const postId =  signal( '123');
let controller;

effect(() => {
    if (controller) {
         controller.abort();
    }
    controller = new AbortController();
    const signal = controller.signal;
    try {
       fetch(`/posts/${postId.value}`, { signal }).then(res => res.json()).then(post => {
            el.innerText = post.title;
        }); 
    } catch (err) {
       // todo: show error message
    }
});


But this still skips a lot of things we normally want to show like loading states and error states.

import { effect, signal, batch } from "@preact/signals-core";

const el = document.querySelector('#output');
const postId =  signal( '123');
const postData = signal({});
const errorMessage = signal('');
const loading = signal(false);
let controller;

effect(() => {
    if (controller) {
         controller.abort();
    }
    controller = new AbortController();
    const signal = controller.signal;
    batch(() => {
       loading.value = true;
       errorMessage.value = '';
       postData.value = {};
    });
    try {
       fetch(`/posts/${postId.value}`, { signal }).then(res => res.json()).then(post => {
            batch(() => {
                 postData.value = post;
                 loading.value = false;
             });
        }); 
    } catch (err) {
        errorMessage.value = err.message;
    }
});
effect(() =>  {
    if (loading.value) {
        el.innerText = 'Loading...';
    } else if (errorMessage.value) {
        el.innerText = `Error: ${errorMessage.value}`;
    } else {
        el.innerText = postData.value.title;
    }
});


Now we can show the proper states, but this is only for one request...

We could wrap this up in a class to reuse or create a new type of signal that can work with asynchronous data.

AsyncState

We want to have a base class that we can make our loading states easily extend from:

export class AsyncState<T> {
  constructor() {}

  get value(): T | null {
    return null;
  }

  get requireValue(): T {
    throw new Error("Value not set");
  }

  get error(): any {
    return null;
  }

  get isLoading(): boolean {
    return false;
  }

  get hasValue(): boolean {
    return false;
  }

  get hasError(): boolean {
    return false;
  }

  map<R>(builders: {
    onLoading: () => R;
    onError: (error: any) => R;
    onData: (data: T) => R;
  }): R {
    if (this.hasError) {
      return builders.onError(this.error);
    }
    if (this.hasValue) {
      return builders.onData(this.requireValue);
    }
    return builders.onLoading();
  }
}


This class actually comes from a Dart port of preact signals I created.

This allows us to easily check if there is an actual value, error or if it is loading. It also provides an easy builder method to map the state to another value. 🤩

AsyncData

The loading state extends AsyncState and passes the value in the constructor to the overriden methods.

export class AsyncData<T> extends AsyncState<T> {
  private _value: T;

  constructor(value: T) {
    super();
    this._value = value;
  }

  get requireValue(): T {
    return this._value;
  }

  get hasValue(): boolean {
    return true;
  }

  toString() {
    return `AsyncData{${this._value}}`;
  }
}

AsyncLoading

For the loading state we override the methods like AsyncData.

export class AsyncLoading<T> extends AsyncState<T> {
  get value(): T | null {
    return null;
  }

  get isLoading(): boolean {
    return true;
  }

  toString() {
    return `AsyncLoading{}`;
  }
}

AsyncError

For the error state we can pass an object of any type to return the error as value instead of throwing an exception (like Go).

export class AsyncError<T> extends AsyncState<T> {
  private _error: any;

  constructor(error: any) {
    super();
    this._error = error;
  }

  get error(): any {
    return this._error;
  }

  get hasError(): boolean {
    return true;
  }

  toString() {
    return `AsyncError{${this._error}}`;
  }
}

asyncSignal

Now we the state classes created, we can create a function to create an asynchronous signal with all the logic we talked about earlier.

We need to show the sync value at any time and have a way to abort previous requests.

export function asyncSignal<T>(
  cb: () => Promise<T>
): ReadonlySignal<AsyncState<T>> {
  const loading = new AsyncLoading<T>();
  const reset = Symbol("reset");
  const s = signal<AsyncState<T>>(loading);
  const c = computed<Promise<T>>(cb);
  let controller: AbortController | null;
  let abortSignal: AbortSignal | null;

  function execute(cb: Promise<T>, cancel: AbortSignal) {
    (async () => {
      s.value = loading;
      try {
        const result = await new Promise<T>(async (resolve, reject) => {
          if (cancel.aborted) {
            reject(cancel.reason);
          }
          cancel.addEventListener("abort", () => {
            reject(cancel.reason);
          });
          try {
            const result = await cb;
            if (cancel.aborted) {
              reject(cancel.reason);
              return;
            }
            resolve(result);
          } catch (error) {
            reject(error);
          }
        });
        s.value = new AsyncData<T>(result);
      } catch (error) {
        if (error === reset) {
          s.value = loading;
        } else {
          s.value = new AsyncError<T>(error);
        }
      }
    })();
  }

  effect(() => {
    if (controller != null) {
      controller.abort(reset);
    }
    controller = new AbortController();
    abortSignal = controller.signal;
    execute(c.value, abortSignal);
  });

  return s;
}


This makes it very easy to create multiple asynchronous signals and also use it anywhere else you have signals in the application like effects and computeds.

const el = document.querySelector('#output');
const postId =  signal('123');

const result = asyncSignal(() => fetch(`/posts/${postId.value}`).then(res => res.json()));

effect(() => {
   el.innerText = result.value.map({
      onLoading: () => 'Loading...',
      onError: (err) => `Error: ${err}`,
      onData: (post) => post.title, 
   });
});

postId.value = '456';

Conclusion

I have started a Preact Signals GitHub discussion here and you can find a gist with the final source code here. 🎉

This has made working with asynchronous data a lot eaiser to work with and would love to hear your thoughts about ways to improve it 👀

Also if you are curious about how Angular does asynchronous signals you can check out the resource signal and the computedFrom/Async signal.

Weekly Installs
44
Repository
rodydavis/skills
GitHub Stars
40
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass