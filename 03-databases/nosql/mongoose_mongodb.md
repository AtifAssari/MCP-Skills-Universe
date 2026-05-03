---
rating: ⭐⭐
title: mongoose-mongodb
url: https://skills.sh/pluginagentmarketplace/custom-plugin-nodejs/mongoose-mongodb
---

# mongoose-mongodb

skills/pluginagentmarketplace/custom-plugin-nodejs/mongoose-mongodb
mongoose-mongodb
Installation
$ npx skills add https://github.com/pluginagentmarketplace/custom-plugin-nodejs --skill mongoose-mongodb
Summary

MongoDB object modeling in Node.js with schema validation, relationships, and advanced queries.

Covers schema design with field validation, CRUD operations, and relationship management through references and population
Includes middleware hooks, virtual properties, indexes, and aggregation pipelines for complex data transformations
Supports query operators for filtering, logical operations, and regex matching across documents
Best practices include environment-based connection management, lean queries for performance, and transaction support for multi-document operations
SKILL.md
Mongoose & MongoDB Skill

Master MongoDB database integration in Node.js with Mongoose, the elegant object modeling library.

Quick Start

Connect and CRUD in 4 steps:

Install - npm install mongoose
Connect - mongoose.connect(uri)
Define Schema - Create data models
CRUD - Create, Read, Update, Delete
Core Concepts
Connection Setup
const mongoose = require('mongoose');

mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

mongoose.connection.on('connected', () => {
  console.log('MongoDB connected');
});

Schema & Model
const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, 'Name is required'],
    trim: true,
    minlength: 3,
    maxlength: 50
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true
  },
  age: {
    type: Number,
    min: 18,
    max: 120
  },
  role: {
    type: String,
    enum: ['user', 'admin'],
    default: 'user'
  }
}, {
  timestamps: true  // createdAt, updatedAt
});

const User = mongoose.model('User', userSchema);

CRUD Operations
// Create
const user = await User.create({
  name: 'John Doe',
  email: 'john@example.com'
});

// Read
const users = await User.find({ age: { $gte: 18 } });
const user = await User.findById(id);
const user = await User.findOne({ email: 'john@example.com' });

// Update
const updated = await User.findByIdAndUpdate(
  id,
  { name: 'Jane Doe' },
  { new: true, runValidators: true }
);

// Delete
await User.findByIdAndDelete(id);
await User.deleteMany({ age: { $lt: 18 } });

Relationships & Population
const postSchema = new mongoose.Schema({
  title: String,
  content: String,
  author: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  }
});

// Populate relationship
const post = await Post.findById(id).populate('author');
// post.author is now full user object

Learning Path
Beginner (2-3 weeks)
✅ Install MongoDB and Mongoose
✅ Create schemas and models
✅ CRUD operations
✅ Basic queries
Intermediate (4-5 weeks)
✅ Relationships and population
✅ Validation and middleware
✅ Indexes for performance
✅ Query operators
Advanced (6-8 weeks)
✅ Aggregation pipelines
✅ Transactions
✅ Schema design patterns
✅ Performance optimization
Advanced Features
Indexes
userSchema.index({ email: 1 }, { unique: true });
userSchema.index({ name: 1, age: -1 });

Middleware (Hooks)
userSchema.pre('save', async function(next) {
  if (this.isModified('password')) {
    this.password = await bcrypt.hash(this.password, 10);
  }
  next();
});

Virtual Properties
userSchema.virtual('fullName').get(function() {
  return `${this.firstName} ${this.lastName}`;
});

Aggregation Pipeline
const stats = await User.aggregate([
  { $match: { age: { $gte: 18 } } },
  { $group: {
    _id: '$role',
    count: { $sum: 1 },
    avgAge: { $avg: '$age' }
  }},
  { $sort: { count: -1 } }
]);

Query Operators
// Comparison
User.find({ age: { $gt: 18 } })     // Greater than
User.find({ age: { $gte: 18 } })    // Greater or equal
User.find({ age: { $lt: 65 } })     // Less than
User.find({ age: { $lte: 65 } })    // Less or equal
User.find({ age: { $ne: 30 } })     // Not equal

// Logical
User.find({ $and: [{ age: { $gte: 18 } }, { age: { $lte: 65 } }] })
User.find({ $or: [{ role: 'admin' }, { role: 'moderator' }] })

// Array
User.find({ tags: { $in: ['node', 'mongodb'] } })
User.find({ tags: { $nin: ['deprecated'] } })

// Regex
User.find({ email: /gmail\.com$/ })

Best Practices
✅ Use environment variables for connection strings
✅ Create indexes for frequently queried fields
✅ Use lean() for read-only queries (better performance)
✅ Validate data at schema level
✅ Use transactions for multi-document operations
✅ Handle connection errors properly
✅ Close connections on app shutdown
When to Use

Use MongoDB with Mongoose when:

Building Node.js applications
Need flexible schema (document-based)
Handling large volumes of data
Rapid prototyping and iteration
Working with JSON-like data
Related Skills
Express REST API (connect to MongoDB)
Async Programming (async database operations)
JWT Authentication (store users)
Jest Testing (test database operations)
Resources
Mongoose Documentation
MongoDB Manual
Schema Design Patterns
Weekly Installs
480
Repository
pluginagentmark…n-nodejs
GitHub Stars
2
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass