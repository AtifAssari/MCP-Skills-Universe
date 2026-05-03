---
title: axios
url: https://skills.sh/slanycukr/riot-api-project/axios
---

# axios

skills/slanycukr/riot-api-project/axios
axios
Installation
$ npx skills add https://github.com/slanycukr/riot-api-project --skill axios
SKILL.md
Axios HTTP Client

Axios is a promise-based HTTP client for the browser and Node.js. It provides a simple API for making HTTP requests and handling responses.

Quick Start
Basic GET Request
import axios from "axios";

// Promise-based
axios
  .get("/user?ID=12345")
  .then((response) => console.log(response.data))
  .catch((error) => console.error(error));

// Async/await
async function getUser() {
  try {
    const response = await axios.get("/user?ID=12345");
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

Basic POST Request
axios
  .post("/user", {
    firstName: "John",
    lastName: "Doe",
  })
  .then((response) => console.log(response.data))
  .catch((error) => console.error(error));

Common Patterns
Custom Instance
const api = axios.create({
  baseURL: "https://api.example.com",
  timeout: 1000,
  headers: { "X-Custom-Header": "foobar" },
});

// Use the instance
api.get("/users").then((response) => console.log(response.data));

Request with Configuration
axios({
  method: "post",
  url: "/user/12345",
  data: {
    firstName: "Fred",
    lastName: "Flintstone",
  },
  headers: {
    "Content-Type": "application/json",
    Authorization: "Bearer token",
  },
});

Concurrent Requests
function getUserAccount() {
  return axios.get("/user/12345");
}

function getUserPermissions() {
  return axios.get("/user/12345/permissions");
}

Promise.all([getUserAccount(), getUserPermissions()]).then(
  ([account, permissions]) => {
    console.log("Account:", account.data);
    console.log("Permissions:", permissions.data);
  },
);

Error Handling
Basic Error Handling
axios.get("/user/12345").catch(function (error) {
  if (error.response) {
    // Server responded with error status
    console.log(error.response.data);
    console.log(error.response.status);
    console.log(error.response.headers);
  } else if (error.request) {
    // Request was made but no response received
    console.log(error.request);
  } else {
    // Error in request setup
    console.log("Error", error.message);
  }
});

Custom Error Status Validation
axios.get("/user/12345", {
  validateStatus: function (status) {
    return status < 500; // Resolve only if status < 500
  },
});

Interceptors
Request Interceptor
axios.interceptors.request.use(
  (config) => {
    // Add auth token to headers
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  },
);

Response Interceptor
axios.interceptors.response.use(
  (response) => {
    // Transform response data
    return response.data;
  },
  (error) => {
    // Handle common errors
    if (error.response?.status === 401) {
      // Redirect to login
      window.location.href = "/login";
    }
    return Promise.reject(error);
  },
);

Authentication Retry Pattern
const api = axios.create({ baseURL: "/api" });

api.interceptors.response.use(undefined, async (error) => {
  if (error.response?.status === 401) {
    await refreshToken();
    return api(error.config); // Retry original request
  }
  throw error;
});

Request/Response Configuration
Common Configuration Options
const config = {
  url: "/user",
  method: "get",
  baseURL: "https://api.example.com",
  headers: { "X-Requested-With": "XMLHttpRequest" },
  params: { ID: 12345 },
  data: { firstName: "John" },
  timeout: 5000,
  responseType: "json",
  withCredentials: false,
  validateStatus: (status) => status >= 200 && status < 300,
};

FormData Upload
const formData = new FormData();
formData.append("file", fileInput.files[0]);
formData.append("username", "john");

axios.post("/upload", formData, {
  headers: {
    "Content-Type": "multipart/form-data",
  },
});

Download Progress
axios.get("/download/file", {
  onDownloadProgress: (progressEvent) => {
    const percentCompleted = Math.round(
      (progressEvent.loaded * 100) / progressEvent.total,
    );
    console.log(`Download: ${percentCompleted}%`);
  },
});

Response Schema

Axios responses contain:

{
  data: {}, // Server response data
  status: 200, // HTTP status code
  statusText: 'OK', // HTTP status message
  headers: {}, // Response headers
  config: {}, // Request config
  request: {} // Request object
}

Best Practices
Use instances for different APIs or configurations
Implement interceptors for auth, logging, and error handling
Set timeouts to prevent hanging requests
Handle errors at appropriate levels
Use TypeScript for better type safety
Cancel requests when components unmount
TypeScript Support
import axios, { AxiosResponse } from "axios";

interface User {
  id: number;
  name: string;
  email: string;
}

const response: AxiosResponse<User> = await axios.get<User>("/user/123");
const user: User = response.data;

Weekly Installs
128
Repository
slanycukr/riot-…-project
GitHub Stars
2
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass