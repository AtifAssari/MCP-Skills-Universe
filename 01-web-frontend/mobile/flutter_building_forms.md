---
rating: ⭐⭐
title: flutter-building-forms
url: https://skills.sh/flutter/skills/flutter-building-forms
---

# flutter-building-forms

skills/flutter/skills/flutter-building-forms
flutter-building-forms
Installation
$ npx skills add https://github.com/flutter/skills --skill flutter-building-forms
Summary

Validated Flutter forms with field-level error handling and submission workflows.

Requires StatefulWidget hosting with a persistent GlobalKey<FormState> to manage form state and validation across rebuilds
Use TextFormField widgets with validator() callbacks that return error strings on failure or null on success
Call _formKey.currentState!.validate() on submit to trigger all validators and automatically display error messages below fields
Includes complete code example demonstrating username validation, error feedback, and success handling via SnackBar
SKILL.md
Building Validated Forms
Contents
Form Architecture
Field Validation
Workflow: Implementing a Validated Form
Examples
Form Architecture

Implement forms using a Form widget to group and validate multiple input fields together.

Use a StatefulWidget: Always host your Form inside a StatefulWidget.
Persist the GlobalKey: Instantiate a GlobalKey<FormState> exactly once as a final variable within the State class. Do not generate a new GlobalKey inside the build method; doing so is resource-expensive and destroys the form's state on every rebuild.
Bind the Key: Pass the GlobalKey<FormState> to the key property of the Form widget. This uniquely identifies the form and provides access to the FormState for validation and submission.
Alternative Access: If dealing with highly complex widget trees where passing the key is impractical, use Form.of(context) to access the FormState from a descendant widget.
Field Validation

Use TextFormField to render Material Design text inputs with built-in validation support. TextFormField is a convenience widget that automatically wraps a standard TextField inside a FormField.

Implement the Validator: Provide a validator() callback function to each TextFormField.
Return Error Messages: If the user's input is invalid, return a String containing the specific error message. The Form will automatically rebuild to display this text below the field.
Return Null for Success: If the input passes validation, you must return null.
Workflow: Implementing a Validated Form

Follow this sequential workflow to implement and validate a form. Copy the checklist to track your progress.

Task Progress:

 1. Create a StatefulWidget and its corresponding State class.
 2. Instantiate final _formKey = GlobalKey<FormState>(); in the State class.
 3. Return a Form widget in the build method and assign key: _formKey.
 4. Add TextFormField widgets as descendants of the Form.
 5. Write a validator function for each TextFormField (return String on error, null on success).
 6. Add a submit button (e.g., ElevatedButton).
 7. Implement the validation check in the button's onPressed callback using _formKey.currentState!.validate().
Validation Decision Logic

When the user triggers the submit action, execute the following conditional logic:

Call _formKey.currentState!.validate().
If true (Valid): All validators returned null. Proceed with form submission (e.g., save data, make API call) and display a success indicator (e.g., a SnackBar).
If false (Invalid): One or more validators returned an error string. The FormState automatically rebuilds the UI to display the error messages.
Feedback Loop: Run validator -> review errors -> fix. The user must adjust their input and resubmit until validate() returns true.
Examples
Complete Validated Form Implementation

Use the following pattern to implement a robust, validated form.

import 'package:flutter/material.dart';

class UserRegistrationForm extends StatefulWidget {
  const UserRegistrationForm({super.key});

  @override
  State<UserRegistrationForm> createState() => _UserRegistrationFormState();
}

class _UserRegistrationFormState extends State<UserRegistrationForm> {
  // 1. Persist the GlobalKey in the State class
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    // 2. Bind the key to the Form
    return Form(
      key: _formKey,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // 3. Add TextFormFields with validators
          TextFormField(
            decoration: const InputDecoration(
              labelText: 'Username',
              hintText: 'Enter your username',
            ),
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter a username'; // Error state
              }
              if (value.length < 4) {
                return 'Username must be at least 4 characters'; // Error state
              }
              return null; // Valid state
            },
          ),
          const SizedBox(height: 16),
          // 4. Add the submit button
          ElevatedButton(
            onPressed: () {
              // 5. Trigger validation logic
              if (_formKey.currentState!.validate()) {
                // Form is valid: Process data
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('Processing Data')),
                );
              } else {
                // Form is invalid: Errors are automatically displayed
                debugPrint('Form validation failed.');
              }
            },
            child: const Text('Submit'),
          ),
        ],
      ),
    );
  }
}

Weekly Installs
8.6K
Repository
flutter/skills
GitHub Stars
1.3K
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass