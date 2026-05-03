---
title: recipe-create-classroom-course
url: https://skills.sh/googleworkspace/cli/recipe-create-classroom-course
---

# recipe-create-classroom-course

skills/googleworkspace/cli/recipe-create-classroom-course
recipe-create-classroom-course
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-create-classroom-course
Summary

Automate Google Classroom course creation and student enrollment workflows.

Creates courses with customizable name, section, room, and owner details via the gws-classroom skill
Invites students by email with role assignment (e.g., STUDENT) and lists enrolled participants
Requires the gws-classroom skill as a prerequisite dependency
SKILL.md
Create a Google Classroom Course

PREREQUISITE: Load the following skills to execute this recipe: gws-classroom

Create a Google Classroom course and invite students.

Steps
Create the course: gws classroom courses create --json '{"name": "Introduction to CS", "section": "Period 1", "room": "Room 101", "ownerId": "me"}'
Invite a student: gws classroom invitations create --json '{"courseId": "COURSE_ID", "userId": "student@school.edu", "role": "STUDENT"}'
List enrolled students: gws classroom courses students list --params '{"courseId": "COURSE_ID"}' --format table
Weekly Installs
10.7K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass