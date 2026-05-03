---
title: jquery
url: https://skills.sh/btafoya/jquery-agent-skill/jquery
---

# jquery

skills/btafoya/jquery-agent-skill/jquery
jquery
Installation
$ npx skills add https://github.com/btafoya/jquery-agent-skill --skill jquery
SKILL.md
jQuery

jQuery is a fast, small, and feature-rich JavaScript library that makes HTML document traversal and manipulation, event handling, animation, and AJAX much simpler with an easy-to-use API that works across a multitude of browsers.

When to Use This Skill

This skill should be used when the user:

Mentions jQuery, $, or jQuery syntax patterns
Asks about DOM manipulation using selectors like $('#id') or $('.class')
Works with event handlers like .on(), .click(), .submit(), .hover()
Needs help with AJAX requests using $.ajax(), $.get(), $.post(), or $.getJSON()
Wants to add animations or effects like .fadeIn(), .slideUp(), .animate()
Asks about jQuery plugins or extending $.fn
Needs to debug jQuery code or fix common issues
Wants to migrate jQuery code to vanilla JavaScript
Asks about jQuery utilities like $.each(), $.map(), $.extend()
Needs help with the jQuery object, chaining, or deferred promises
Core Concepts
The jQuery Object $ and jQuery

The global function $ (and its alias jQuery) is the entry point for all jQuery operations. It returns a jQuery object (often called a "wrapped set") containing matched DOM elements.

// These are equivalent
$('#myElement')
jQuery('#myElement')

// The jQuery object is array-like
var $el = $('#myElement');
console.log($el.length); // Number of matched elements
console.log($el[0]);      // First DOM element (unwrapped)

Ready Handler

Always wrap jQuery code in a document ready handler to ensure the DOM is fully loaded:

// Shorthand
$(document).ready(function() {
    // Your code here
});

// Or shorter
$(function() {
    // Your code here
});

Chaining

jQuery methods return the jQuery object, enabling method chaining:

$('#myElement')
    .addClass('highlight')
    .css('color', 'red')
    .fadeIn(300)
    .on('click', handleClick);

Selectors

jQuery uses CSS-like selectors to find elements:

// Basic selectors
$('#id')              // ID selector
$('.class')           // Class selector
$('div')              // Element selector
$('*')                // Universal selector

// Multiple selectors
$('#id, .class, div') // Comma-separated

// Hierarchy
$('div p')            // Descendant
$('div > p')          // Direct child
$('div + p')          // Adjacent sibling
$('div ~ p')          // General sibling

// Attribute
$('[data-id]')        // Has attribute
$('[data-id="123"]')  // Attribute equals
$('input[type="text"]')

// Filters
$('li:first')         // First element
$('li:last')          // Last element
$('li:even')          // Even-indexed elements
$('li:odd')           // Odd-indexed elements
$('li:eq(2)')         // Element at index 2
$('li:gt(2)')         // Elements after index 2
$('li:lt(5)')         // Elements before index 5
$('li:not(.exclude)') // Negation

// Form selectors
$(':input')           // All form elements
$(':text')            // Text inputs
$(':checkbox')        // Checkboxes
$(':checked')         // Checked elements
$(':selected')        // Selected elements
$(':disabled')        // Disabled elements

DOM Manipulation
Getting and Setting Content
// Get/set HTML
$('#myDiv').html();                   // Get innerHTML
$('#myDiv').html('<p>New content</p>'); // Set innerHTML

// Get/set text
$('#myDiv').text();                   // Get text content
$('#myDiv').text('New text');         // Set text content

// Get/set form values
$('#myInput').val();                  // Get value
$('#myInput').val('New value');       // Set value

// Get/set attributes
$('#myImage').attr('src');            // Get attribute
$('#myImage').attr('src', 'new.jpg'); // Set attribute
$('#myImage').removeAttr('alt');      // Remove attribute

// Get/set data attributes
$('#myDiv').data('id');               // Get data-* value
$('#myDiv').data('id', '123');        // Set data-* value

Modifying Elements
// Classes
$('#myDiv').addClass('highlight');           // Add class
$('#myDiv').removeClass('highlight');        // Remove class
$('#myDiv').toggleClass('active');           // Toggle class
$('#myDiv').hasClass('active');              // Check if has class

// CSS
$('#myDiv').css('color', 'red');             // Set single property
$('#myDiv').css({
    'color': 'red',
    'background': 'blue',
    'padding': '10px'
});                                          // Set multiple properties
$('#myDiv').css('color');                    // Get property

// Dimensions
$('#myDiv').width();                         // Inner width
$('#myDiv').height();                        // Inner height
$('#myDiv').innerWidth();                    // Inner width + padding
$('#myDiv').innerHeight();                   // Inner height + padding
$('#myDiv').outerWidth();                    // Width + padding + border
$('#myDiv').outerHeight();                   // Height + padding + border
$('#myDiv').outerWidth(true);                // Include margin

// Position
$('#myDiv').offset();                        // Position relative to document
$('#myDiv').position();                      // Position relative to parent
$('#myDiv').offset({ top: 100, left: 50 });  // Set position

// Scrolling
$(window).scrollTop();                       // Get scroll position
$(window).scrollTop(200);                    // Set scroll position

Creating and Inserting Elements
// Create element
var $newDiv = $('<div class="new">Content</div>');

// Insert methods
$parent.append($newDiv);      // Append to end of parent
$parent.prepend($newDiv);     // Prepend to beginning of parent
$newDiv.appendTo($parent);    // Append this element to parent
$newDiv.prependTo($parent);   // Prepend this element to parent

$element.after($newDiv);      // Insert after element
$element.before($newDiv);     // Insert before element
$newDiv.insertAfter($element);
$newDiv.insertBefore($element);

// Wrap
$element.wrap('<div class="wrapper"></div>');
$elements.wrapAll('<div class="wrapper"></div>');
$element.wrapInner('<span></span>');

// Remove
$element.remove();            // Remove element from DOM
$element.empty();             // Remove all children
$element.detach();            // Remove but keep data/events

// Replace
$element.replaceWith('<div>Replacement</div>');

Traversing
// Filtering
$('li').first();              // First element
$('li').last();               // Last element
$('li').eq(2);                // Element at index 2
$('li').filter('.active');    // Filter by selector
$('li').not('.exclude');      // Exclude elements
$('li').has('.child');        // Has descendant matching selector
$('li').slice(1, 4);          // Slice elements

// Finding
$('#parent').find('.child');  // Find descendants
$element.children();          // Direct children only
$element.children('.active'); // Direct children matching selector

// Relationships
$element.parent();            // Direct parent
$element.parents();           // All ancestors
$element.parentsUntil('.container'); // Ancestors until match
$element.closest('.ancestor'); // Closest ancestor (includes self)
$element.siblings();          // All siblings
$element.siblings('.active'); // Siblings matching selector
$element.next();              // Next sibling
$element.nextAll();           // All next siblings
$element.nextUntil('.stop');  // Next siblings until match
$element.prev();              // Previous sibling
$element.prevAll();           // All previous siblings
$element.prevUntil('.stop');  // Previous siblings until match

Event Handling
Binding Events
// Basic event binding
$('#myButton').click(function() {
    console.log('Clicked!');
});

// Shorthand methods available for most events:
// .click(), .dblclick(), .mouseenter(), .mouseleave(),
// .mouseover(), .mouseout(), .mousedown(), .mouseup(),
// .mousemove(), .keydown(), .keyup(), .keypress(),
// .submit(), .change(), .focus(), .blur(), .scroll()

// Using .on() for all events
$('#myButton').on('click', function(event) {
    event.preventDefault(); // Prevent default behavior
    event.stopPropagation(); // Stop event bubbling
    console.log('Clicked!', event);
});

// Multiple events
$('#myButton').on('click mouseenter', function() {
    $(this).addClass('active');
});

// Event-specific handler
$('#myButton').on({
    click: function() { console.log('Clicked'); },
    mouseenter: function() { console.log('Entered'); }
});

// Pass data to handler
$('#myButton').on('click', { name: 'John' }, function(event) {
    console.log('Hello, ' + event.data.name);
});

// Event delegation (for dynamically added elements)
$(document).on('click', '.dynamic-button', function() {
    console.log('Dynamic button clicked!');
});

Unbinding Events
// Remove specific handler
$('#myButton').off('click', myHandler);

// Remove all click handlers
$('#myButton').off('click');

// Remove all event handlers
$('#myButton').off();

Event Object
$('#myElement').on('click keypress', function(event) {
    console.log('Event type:', event.type);
    console.log('Target:', event.target);
    console.log('Current target:', event.currentTarget);
    console.log('Timestamp:', event.timeStamp);
    console.log('Which:', event.which); // For key/button codes

    // Keyboard events
    if (event.type === 'keypress') {
        console.log('Key:', event.key);
        console.log('Code:', event.code);
    }

    // Mouse events
    if (event.type === 'click') {
        console.log('Page X:', event.pageX);
        console.log('Page Y:', event.pageY);
        console.log('Client X:', event.clientX);
        console.log('Client Y:', event.clientY);
    }
});

Utility Events
// One-time event
$('#myButton').one('click', function() {
    console.log('Will only fire once');
});

// Trigger events programmatically
$('#myButton').trigger('click');
$('#myButton').click(); // Shorthand

// Custom events
$(document).on('customEvent', function(event, param1, param2) {
    console.log(param1, param2);
});
$('#myButton').trigger('customEvent', ['hello', 'world']);

AJAX and HTTP Requests
Basic AJAX
// Basic $.ajax()
$.ajax({
    url: '/api/data',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
        console.log('Success:', data);
    },
    error: function(xhr, status, error) {
        console.error('Error:', error);
    },
    complete: function(xhr, status) {
        console.log('Request complete');
    }
});

// Promise-style (jQuery 3+)
$.ajax({
    url: '/api/data',
    method: 'GET',
    dataType: 'json'
})
.done(function(data) {
    console.log('Success:', data);
})
.fail(function(xhr, status, error) {
    console.error('Error:', error);
})
.always(function() {
    console.log('Always runs');
});

Shorthand Methods
// GET request
$.get('/api/data', function(data) {
    console.log(data);
});

// GET with parameters
$.get('/api/data', { id: 123, name: 'John' }, function(data) {
    console.log(data);
});

// POST request
$.post('/api/data', { name: 'John', email: 'john@example.com' }, function(data) {
    console.log(data);
});

// GET JSON
$.getJSON('/api/data.json', function(data) {
    console.log(data);
});

// Load HTML into element
$('#result').load('/api/content #section');

AJAX Configuration
$.ajax({
    url: '/api/data',
    method: 'POST',
    dataType: 'json',
    contentType: 'application/json',
    data: JSON.stringify({ name: 'John' }),

    // Advanced options
    timeout: 5000,
    async: true,
    cache: false,
    headers: {
        'X-Custom-Header': 'value'
    },
    beforeSend: function(xhr) {
        xhr.setRequestHeader('Authorization', 'Bearer token');
    },

    // Response handling
    statusCode: {
        404: function() {
            console.log('Not found');
        },
        500: function() {
            console.log('Server error');
        }
    }
});

Global AJAX Events
// Show/hide loading indicator
$(document)
    .ajaxStart(function() {
        $('#loading').show();
    })
    .ajaxStop(function() {
        $('#loading').hide();
    })
    .ajaxError(function(event, xhr, settings, error) {
        console.error('AJAX error:', error);
    })
    .ajaxSuccess(function(event, xhr, settings) {
        console.log('AJAX success');
    });

AJAX Setup
// Set default AJAX options
$.ajaxSetup({
    timeout: 10000,
    error: function(xhr, status, error) {
        console.error('Default error handler:', error);
    }
});

// Prefilter requests
$.ajaxPrefilter(function(options, originalOptions, xhr) {
    if (options.url.match(/^\/api\//)) {
        options.headers = options.headers || {};
        options.headers['Authorization'] = 'Bearer ' + getToken();
    }
});

Animations and Effects
Basic Effects
// Show/Hide
$('#myElement').show();           // Show element
$('#myElement').hide();           // Hide element
$('#myElement').toggle();         // Toggle visibility
$('#myElement').show(500);        // Animate show with duration (ms)
$('#myElement').show('slow');     // 'slow', 'normal', 'fast'

// Fade
$('#myElement').fadeIn();         // Fade in
$('#myElement').fadeOut();        // Fade out
$('#myElement').fadeToggle();     // Toggle fade
$('#myElement').fadeTo(500, 0.5); // Fade to opacity (duration, opacity)

// Slide
$('#myElement').slideDown();      // Slide down
$('#myElement').slideUp();        // Slide up
$('#myElement').slideToggle();    // Toggle slide

Custom Animations
// Animate CSS properties
$('#myElement').animate({
    opacity: 0.5,
    width: '200px',
    height: '200px',
    left: '100px',
    top: '100px'
}, 1000);

// Animation with options
$('#myElement').animate(
    { width: 'toggle' },
    {
        duration: 1000,
        easing: 'swing', // 'swing' or 'linear'
        complete: function() {
            console.log('Animation complete');
        },
        step: function(now, fx) {
            console.log('Current value:', now);
        },
        queue: true
    }
);

// Parallel animations
$('#myElement')
    .animate({ width: '200px' }, 1000)
    .animate({ height: '200px' }, 1000);

Animation Control
var $el = $('#myElement');

// Stop animation
$el.stop();                      // Stop current animation
$el.stop(true);                  // Clear queue and stop
$el.stop(true, true);            // Jump to end

// Check if animating
if ($el.is(':animated')) {
    console.log('Currently animating');
}

// Delay
$el.fadeOut(300).delay(500).fadeIn(300);

// Disable queue
$el.animate({ left: '+=100' }, { queue: false });

Utilities
Array/Object Utilities
// Each
$.each([1, 2, 3], function(index, value) {
    console.log(index + ': ' + value);
});

$.each({ name: 'John', age: 30 }, function(key, value) {
    console.log(key + ': ' + value);
});

// Map
var doubled = $.map([1, 2, 3], function(value, index) {
    return value * 2;
}); // [2, 4, 6]

// Grep (filter)
var even = $.grep([1, 2, 3, 4, 5], function(value) {
    return value % 2 === 0;
}); // [2, 4]

// Extend (merge objects)
var obj1 = { name: 'John' };
var obj2 = { age: 30 };
var merged = $.extend({}, obj1, obj2); // { name: 'John', age: 30 }

// Deep extend
var obj1 = { user: { name: 'John' } };
var obj2 = { user: { age: 30 } };
var merged = $.extend(true, {}, obj1, obj2); // { user: { name: 'John', age: 30 } }

// Make array
var nodes = $('div').get(); // Returns array of DOM elements
var first = $('div').get(0); // Returns first DOM element

// Index
var index = $('li').index($('#myLi')); // Get index of element

String Utilities
// Trim
var trimmed = $.trim('  hello  '); // 'hello'

// Parse JSON
var obj = $.parseJSON('{"name":"John"}');

// Serialize (form)
var queryString = $('#myForm').serialize(); // name=John&age=30
var data = $('#myForm').serializeArray(); // Array of objects

// Param (object to query string)
var queryString = $.param({ name: 'John', age: 30 }); // name=John&age=30

Type Checking
$.isFunction(function() {});   // true
$.isArray([1, 2, 3]);         // true
$.isPlainObject({});          // true
$.isNumeric(123);             // true
$.isNumeric('123');           // true
$.isEmptyObject({});          // true
$.isWindow(window);           // true

Deferred and Promises
Basic Deferred
function asyncTask() {
    var deferred = $.Deferred();

    setTimeout(function() {
        deferred.resolve('Success!');
    }, 1000);

    return deferred.promise();
}

asyncTask()
    .done(function(result) {
        console.log(result);
    })
    .fail(function(error) {
        console.error(error);
    })
    .always(function() {
        console.log('Always runs');
    });

When (Parallel)
$.when(asyncTask1(), asyncTask2())
    .done(function(result1, result2) {
        console.log('All done:', result1, result2);
    })
    .fail(function() {
        console.error('One or more failed');
    });

Promise Methods
// then
asyncTask().then(
    function(result) {
        // Success callback
    },
    function(error) {
        // Error callback
    }
);

// pipe (chaining)
asyncTask()
    .pipe(function(result) {
        return asyncTask2(result);
    })
    .done(function(finalResult) {
        console.log(finalResult);
    });

Plugin Development
Basic Plugin Pattern
// Attach plugin to $.fn (jQuery prototype)
(function($) {
    $.fn.highlight = function(options) {
        // Default settings
        var settings = $.extend({
            color: 'yellow',
            duration: 500
        }, options);

        // Return this for chaining
        return this.each(function() {
            var $this = $(this);
            $this.css('background-color', settings.color);
            $this.fadeIn(settings.duration);
        });
    };
})(jQuery);

// Usage
$('#myElement').highlight({ color: 'red', duration: 1000 });

Plugin with Public Methods
(function($) {
    var methods = {
        init: function(options) {
            var settings = $.extend({
                color: 'yellow'
            }, options);
            return this.each(function() {
                var $this = $(this);
                $this.data('highlight', settings);
                $this.css('background-color', settings.color);
            });
        },
        destroy: function() {
            return this.each(function() {
                $(this).removeData('highlight');
            });
        },
        color: function(newColor) {
            if (newColor) {
                return this.each(function() {
                    $(this).css('background-color', newColor);
                });
            }
            return this.css('background-color');
        }
    };

    $.fn.highlight = function(method) {
        if (methods[method]) {
            return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
        } else if (typeof method === 'object' || !method) {
            return methods.init.apply(this, arguments);
        } else {
            $.error('Method ' + method + ' does not exist');
        }
    };
})(jQuery);

// Usage
$('#myElement').highlight({ color: 'red' });
$('#myElement').highlight('color', 'blue');
$('#myElement').highlight('destroy');

Widget Factory (jQuery UI pattern)

If using jQuery UI, use the widget factory:

$.widget('custom.highlighter', {
    options: {
        color: 'yellow'
    },
    _create: function() {
        this.element.css('background-color', this.options.color);
    },
    _setOption: function(key, value) {
        if (key === 'color') {
            this.element.css('background-color', value);
        }
        this._super(key, value);
    },
    color: function(newColor) {
        if (newColor) {
            this._setOption('color', newColor);
        }
        return this.options.color;
    }
});

// Usage
$('#myElement').highlighter({ color: 'red' });
$('#myElement').highlighter('color', 'blue');

Best Practices
Performance
// Cache jQuery selectors
var $button = $('#myButton');
$button.on('click', handleClick);

// Use find() instead of context (faster in newer jQuery)
$('#container').find('.item'); // Better than $('.item', '#container')

// Use event delegation for many elements
$(document).on('click', '.dynamic-item', handleClick); // Better than binding to each

// Use .end() to return to previous state in chains
$('#container')
    .find('.item')
        .addClass('active')
    .end()
    .addClass('container-active');

// Minimize DOM reflows by batching changes
var $items = $('.item');
$items.css('opacity', 0); // Single reflow instead of many

// Use document fragment for multiple insertions
var fragment = document.createDocumentFragment();
$.each(items, function(i, item) {
    fragment.appendChild(item);
});
$('#container').append(fragment);

Safety
// Check if element exists
if ($('#myElement').length) {
    // Element exists
}

// Use $(this) carefully inside nested functions
$('#myButton').on('click', function() {
    var $this = $(this);
    setTimeout(function() {
        $this.addClass('clicked'); // $this still refers to button
    }, 100);
});

Namespace Events
// Namespaced events for easier cleanup
$('#myButton').on('click.myNamespace', handleClick);
$('#myButton').off('.myNamespace'); // Remove all events in namespace

// Multiple namespaces
$('#myButton').on('click.app.submit', handleSubmit);

Avoid Global Variables
// Wrap code in IIFE
(function($) {
    // Your code here
    var privateVariable = 'local';

    $('#myButton').on('click', function() {
        console.log(privateVariable);
    });
})(jQuery);

Common Patterns
Form Validation
$('#myForm').on('submit', function(e) {
    e.preventDefault();
    var $form = $(this);
    var isValid = true;

    $form.find('input[required]').each(function() {
        var $input = $(this);
        if (!$input.val().trim()) {
            $input.addClass('error');
            isValid = false;
        } else {
            $input.removeClass('error');
        }
    });

    if (isValid) {
        $.ajax({
            url: $form.attr('action'),
            method: $form.attr('method'),
            data: $form.serialize(),
            success: function(response) {
                console.log('Form submitted successfully');
            }
        });
    }
});

Infinite Scroll
$(window).on('scroll', function() {
    if ($(window).scrollTop() + $(window).height() >= $(document).height() - 100) {
        loadMoreItems();
    }
});

Modal Dialog
$('#openModal').on('click', function() {
    $('#modal').fadeIn(300).addClass('open');
});

$('#modal').on('click', function(e) {
    if ($(e.target).is('#modal') || $(e.target).is('.close')) {
        $(this).fadeOut(300).removeClass('open');
    }
});

Tab Navigation
$('.tab').on('click', function(e) {
    e.preventDefault();
    var $tab = $(this);
    var target = $tab.data('target');

    $('.tab').removeClass('active');
    $('.tab-content').removeClass('active');

    $tab.addClass('active');
    $(target).addClass('active');
});

Debugging Tips
// Check if jQuery is loaded
if (typeof jQuery === 'undefined') {
    console.error('jQuery is not loaded!');
}

// Check jQuery version
console.log('jQuery version:', $.fn.jquery);

// Check selector matches
console.log('Matched elements:', $('.my-selector').length);

// Inspect jQuery object
console.dir($('#myElement')); // Shows all methods

// Use $.holdReady() for debugging
$.holdReady(true);
// Load your code, then:
$.holdReady(false);

Migration to Vanilla JavaScript

When helping users migrate from jQuery to vanilla JS, here are common equivalents:

// jQuery → Vanilla JS

// Selectors
$('#id')                    → document.getElementById('id')
$('.class')                 → document.querySelectorAll('.class')
$('div')                    → document.querySelectorAll('div')

// Events
$('.class').on('click', fn) → document.querySelectorAll('.class').forEach(el → el.addEventListener('click', fn))

// Classes
$(el).addClass('class')     → el.classList.add('class')
$(el).removeClass('class')  → el.classList.remove('class')
$(el).toggleClass('class')  → el.classList.toggle('class')

// Content
$(el).html()                → el.innerHTML
$(el).text()                → el.textContent
$(el).val()                 → el.value

// Attributes
$(el).attr('src', 'url')    → el.setAttribute('src', 'url')
$(el).data('id', '123')     → el.dataset.id = '123'

// Styles
$(el).css('color', 'red')   → el.style.color = 'red'

// AJAX
$.ajax(...)                 → fetch(url, options).then(r → r.json())

// Ready handler
$(function() {})            → document.addEventListener('DOMContentLoaded', fn)

Resources
Official jQuery documentation: https://api.jquery.com/
jQuery download: https://jquery.com/download/
Browser support: https://jquery.com/browser-support/
Weekly Installs
38
Repository
btafoya/jquery-…nt-skill
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass