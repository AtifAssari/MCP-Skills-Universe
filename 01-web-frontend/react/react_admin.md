---
title: react-admin
url: https://skills.sh/marmelab/react-admin/react-admin
---

# react-admin

skills/marmelab/react-admin/react-admin
react-admin
Installation
$ npx skills add https://github.com/marmelab/react-admin --skill react-admin
SKILL.md
React-Admin Development Guide

React-admin is a framework for building single-page applications on top of REST/GraphQL APIs. It builds on top of React Query, react-hook-form, react-router, and Material UI. It provides 150+ components and dozens of hooks. Before writing custom code, always check if react-admin already provides a component or hook for the task. Full documentation: https://marmelab.com/react-admin/doc/

Providers (Backend Abstraction)

React-admin never calls APIs directly. All communication goes through providers — adapters that translate react-admin's standardized calls into API-specific requests. The three main providers are:

dataProvider: All CRUD operations (getList, getOne, create, update, delete, getMany, getManyReference, updateMany, deleteMany). See DataProviders and 50+ existing adapters.
authProvider: Authentication and authorization. See Authentication.
i18nProvider: Translations (translate, changeLocale, getLocale).

Critical rule: Never use fetch, axios, or direct HTTP calls in components. Always use data provider hooks. This ensures proper caching, loading states, error handling, authentication, and optimistic rendering.

Composition (Not God Components)

React-admin uses composition over configuration. Override behavior by passing child components, not by setting dozens of props:

<Edit actions={<MyCustomActions />}>
    <SimpleForm>
        <TextInput source="title" />
    </SimpleForm>
</Edit>


To customize the layout, pass a custom layout component to <Admin layout={MyLayout}>. To customize the menu, pass it to <Layout menu={MyMenu}>. This chaining is by design — see Architecture.

Context: Pull, Don't Push

React-admin components expose data to descendants via React contexts. Access data using hooks rather than passing props down:

useRecordContext() — current record in Show/Edit/Create views. See useRecordContext.
useListContext() — list data, filters, pagination, sort in List views. See useListContext.
useShowContext(), useEditContext(), useCreateContext() — page-level state for detail views.
useTranslate() — translation function from i18nProvider.
useGetIdentity() — current user from authProvider.
Hooks Over Custom Components

When a react-admin component's UI doesn't fit, use the underlying hook instead of building from scratch. Controller hooks (named use*Controller) provide all the logic without the UI:

useListController() — list fetching, filtering, pagination logic
useEditController() — edit form fetching and submission logic
useShowController() — show page data fetching logic
Routing

<Resource> declares CRUD routes automatically (/posts, /posts/create, /posts/:id/edit, /posts/:id/show). Use <CustomRoutes> for non-CRUD pages. Use useCreatePath() to build resource URLs and <Link> from react-admin for navigation. Default router is react-router (HashRouter), but TanStack Router is also supported via routerProvider. See Routing.

Data Fetching
Query Hooks (Reading Data)
const { data, total, isPending, error } = useGetList('posts', {
    pagination: { page: 1, perPage: 25 },
    sort: { field: 'created_at', order: 'DESC' },
    filter: { status: 'published' },
});

const { data: record, isPending } = useGetOne('posts', { id: 123 });
const { data: records } = useGetMany('posts', { ids: [1, 2, 3] });
const { data, total } = useGetManyReference('comments', {
    target: 'post_id', id: 123,
    pagination: { page: 1, perPage: 25 },
});


See useGetList, useGetOne.

Mutation Hooks (Writing Data)

All mutations return [mutate, state]. They support three mutation modes:

pessimistic (default): Wait for server response, then update UI.
optimistic: Update UI immediately, revert on server error.
undoable: Update UI, show undo notification, commit after delay.
const [create, { isPending }] = useCreate();
const [update] = useUpdate();
const [deleteOne] = useDelete();

// Call with resource and params
create('posts', { data: { title: 'Hello' } });
update('posts', { id: 1, data: { title: 'Updated' }, previousData: record });
deleteOne('posts', { id: 1, previousData: record });


Pass mutationMode: 'optimistic' or 'undoable' for instant UI feedback. See useCreate, useUpdate.

Authentication & Authorization
const authProvider = {
    login: ({ username, password }) => Promise<void>,
    logout: () => Promise<void>,
    checkAuth: () => Promise<void>,           // Verify credentials are valid
    checkError: (error) => Promise<void>,      // Detect auth errors from API responses
    getIdentity: () => Promise<{ id, fullName, avatar }>,
    getPermissions: () => Promise<any>,
    canAccess: ({ resource, action, record }) => Promise<boolean>,  // RBAC
};


Each auth provider method has a corresponding hook (e.g. useGetIdentity(), useCanAccess()).

Custom routes are public by default. Wrap them with <Authenticated> or call useAuthenticated() to require login. See Authenticated.
Centralize authorization in authProvider.canAccess(), not in individual components. Use useCanAccess() to check permissions. See useCanAccess and AuthRBAC.
The dataProvider must include credentials (Bearer token, cookies) in requests — authProvider handles login, but dataProvider handles API calls. Configure httpClient in data provider setup.
Relationships Between Entities

Fetching all the data (including relationships) upfront for a given page is an anti-pattern. Instead, fetch related records on demand using reference fields and inputs.

Displaying Related Records (Fields)
{/* Show a the company of the current record based on its company_id */}
<ReferenceField source="company_id" reference="companies" />

{/* Show a list of related records (reverse FK) */}
<ReferenceManyField reference="comments" target="post_id">
    <DataTable>
        <TextField source="body" />
        <DateField source="created_at" />
    </DataTable>
</ReferenceManyField>

{/* Show multiple referenced records (array of IDs) */}
<ReferenceArrayField source="tag_ids" reference="tags">
    <SingleFieldList>
        <ChipField source="name" />
    </SingleFieldList>
</ReferenceArrayField>


See ReferenceField, ReferenceManyField, ReferenceArrayField.

Editing Related Records (Inputs)
{/* Select from another resource (FK) */}
<ReferenceInput source="company_id" reference="companies" />

{/* Multi-select from another resource (array of IDs) */}
<ReferenceArrayInput source="tag_ids" reference="tags" />


See ReferenceInput, ReferenceArrayInput.

Forms

React-admin forms are built on react-hook-form. Use <SimpleForm> for single-column layouts and <TabbedForm> for multi-tab layouts. See SimpleForm, TabbedForm.

Pass validators to input components: required(), minLength(min), maxLength(max), minValue(min), maxValue(max), number(), email(), regex(pattern, message), or a custom function returning an error string.

<TextInput source="title" validate={[required(), minLength(3)]} />


Use RHF's useWatch() to create dynamic forms that react to field values:

Resource Definition

Encapsulate resource components in index files for clean imports:

// posts/index.ts
export default {
    list: PostList,
    create: PostCreate,
    edit: PostEdit,
    icon: PostIcon,
    recordRepresentation: (record) => record.title,  // How records appear in references
};


See Resource, RecordRepresentation.

Custom Data Provider Methods

Extend the dataProvider with domain-specific methods:

const dataProvider = {
    ...baseDataProvider,
    archivePost: async (id) => { /* custom logic */ },
};
// Call via useDataProvider and useQuery:
// const dp = useDataProvider(); 
// const { data } = useQuery(['archivePost', id], () => dp.archivePost(id));

Persistent Client State (Store)

Use useStore() for persistent user preferences (theme, column visibility, saved filters):

const [theme, setTheme] = useStore('theme', 'light');


See Store.

Notification, Redirect, Refresh
const notify = useNotify();
const redirect = useRedirect();
const refresh = useRefresh();

notify('Record saved', { type: 'success' });
redirect('list', 'posts');        // Navigate to /posts
redirect('edit', 'posts', 123);   // Navigate to /posts/123
refresh();                         // Invalidate all queries

Deprecations
Use DataTable instead of Datagrid
Prefer <CanAccess> and useCanAccess for authorization checks
Weekly Installs
114
Repository
marmelab/react-admin
GitHub Stars
26.7K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass