---
rating: ⭐⭐
title: karma-skill
url: https://skills.sh/lambdatest/agent-skills/karma-skill
---

# karma-skill

skills/lambdatest/agent-skills/karma-skill
karma-skill
Installation
$ npx skills add https://github.com/lambdatest/agent-skills --skill karma-skill
SKILL.md
Karma Testing Skill
Core Patterns
karma.conf.js
module.exports = function(config) {
  config.set({
    basePath: '',
    frameworks: ['jasmine'],
    files: [
      'src/**/*.js',
      'test/**/*.spec.js'
    ],
    preprocessors: {
      'src/**/*.js': ['coverage']
    },
    reporters: ['progress', 'coverage'],
    coverageReporter: {
      type: 'html',
      dir: 'coverage/'
    },
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    browsers: ['Chrome', 'Firefox'],
    singleRun: false,
    concurrency: Infinity,

    // LambdaTest cloud browsers
    customLaunchers: {
      ChromeLT: {
        base: 'WebDriver',
        config: {
          hostname: 'hub.lambdatest.com',
          port: 80
        },
        browserName: 'Chrome',
        version: 'latest',
        name: 'Karma Test',
        tunnel: true,
        user: process.env.LT_USERNAME,
        accessKey: process.env.LT_ACCESS_KEY
      }
    }
  });
};

Test with Jasmine Framework
describe('StringUtils', () => {
  it('should capitalize first letter', () => {
    expect(StringUtils.capitalize('hello')).toBe('Hello');
  });

  it('should handle empty string', () => {
    expect(StringUtils.capitalize('')).toBe('');
  });
});

Angular Integration
// karma.conf.js for Angular
frameworks: ['jasmine', '@angular-devkit/build-angular'],
plugins: [
  require('karma-jasmine'),
  require('karma-chrome-launcher'),
  require('karma-coverage'),
  require('@angular-devkit/build-angular/plugins/karma')
],

Setup: npm install karma karma-jasmine karma-chrome-launcher karma-coverage --save-dev
Run: npx karma start or npx karma start --single-run
Init: npx karma init karma.conf.js
Deep Patterns

See reference/playbook.md for production-grade patterns:

Section	What You Get
§1 Production Configuration	Full karma.conf.js with coverage thresholds, reporters, CI launchers
§2 Component Testing	Service mocking, DOM interaction, form validation patterns
§3 HTTP Service Testing	HttpTestingController, error handling, retry testing
§4 Directive & Pipe Testing	Host component pattern, custom pipes with edge cases
§5 RxJS & Async Patterns	debounceTime, switchMap cancellation, subscription cleanup
§6 Router & NgRx Testing	RouterTestingModule, MockStore, selector overrides
§7 LambdaTest Integration	Cloud browser configuration for cross-browser testing
§8 CI/CD Integration	GitHub Actions with coverage, test reporting
§9 Debugging Table	12 common problems with causes and fixes
§10 Best Practices	14-item checklist for production Angular testing
Weekly Installs
40
Repository
lambdatest/agent-skills
GitHub Stars
247
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass