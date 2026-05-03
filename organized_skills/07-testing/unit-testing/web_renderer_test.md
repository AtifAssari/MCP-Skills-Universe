---
rating: ⭐⭐
title: web-renderer-test
url: https://skills.sh/remotion-dev/remotion/web-renderer-test
---

# web-renderer-test

skills/remotion-dev/remotion/web-renderer-test
web-renderer-test
Installation
$ npx skills add https://github.com/remotion-dev/remotion --skill web-renderer-test
Summary

Visual snapshot testing for web renderer components using vitest fixtures.

Create test fixtures in packages/web-renderer/src/test/fixtures that define a React component, dimensions, frame rate, and duration
Register fixtures in packages/web-renderer/src/test/Root.tsx to enable preview functionality
Write test cases that render stills using renderStillOnWeb() and validate output with testImage() snapshot comparison
Run tests with bunx vitest src/test/video.test.tsx and update documentation in limitations.mdx when adding new supported properties
SKILL.md

The web renderer is in packages/web-renderer and the test suite is in packages/web-renderer/src/test.

It uses visual snapshot testing using vitest. A test file can for example be executed using:

bunx vitest src/test/video.test.tsx

Example

Each test is powered by a fixture in packages/web-renderer/src/test/fixtures. A fixture looks like this for example:

import {AbsoluteFill} from 'remotion';

const Component: React.FC = () => {
  return (
    <AbsoluteFill
      style={{
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <div
        style={{
          backgroundColor: 'red',
          width: 100,
          height: 100,
          borderRadius: 20,
        }}
      />
    </AbsoluteFill>
  );
};

export const backgroundColor = {
  component: Component,
  id: 'background-color',
  width: 200,
  height: 200,
  fps: 25,
  durationInFrames: 1,
} as const;


The corresponding test looks like this:

import {test} from 'vitest';
import {renderStillOnWeb} from '../render-still-on-web';
import {backgroundColor} from './fixtures/background-color';
import {testImage} from './utils';

test('should render background-color', async () => {
  const blob = await renderStillOnWeb({
    licenseKey: 'free-license',
    composition: backgroundColor,
    frame: 0,
    inputProps: {},
    imageFormat: 'png',
  });

  await testImage({blob, testId: 'background-color'});
});

Adding a new test
Add a new fixture in packages/web-renderer/src/test/fixtures.
Important: Add the fixture to packages/web-renderer/src/test/Root.tsx to add a way to preview it.
Add a new test in packages/web-renderer/src/test.
Run bunx vitest src/test/video.test.tsx to execute the test.
Important: Update packages/docs/docs/client-side-rendering/limitations.mdx to reflect the newly supported property.
Weekly Installs
792
Repository
remotion-dev/remotion
GitHub Stars
45.4K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass