---
title: tanstack-table
url: https://skills.sh/tanstack-skills/tanstack-skills/tanstack-table
---

# tanstack-table

skills/tanstack-skills/tanstack-skills/tanstack-table
tanstack-table
Installation
$ npx skills add https://github.com/tanstack-skills/tanstack-skills --skill tanstack-table
SKILL.md
Overview

TanStack Table is a headless UI library for building data tables and datagrids. It provides logic for sorting, filtering, pagination, grouping, expanding, column pinning/ordering/visibility/resizing, and row selection - without rendering any markup or styles.

Package: @tanstack/react-table Utilities: @tanstack/match-sorter-utils (fuzzy filtering) Current Version: v8

Installation
npm install @tanstack/react-table

Core Architecture
Building Blocks
Column Definitions - describe columns (data access, rendering, features)
Table Instance - central coordinator with state and APIs
Row Models - data processing pipeline (filter -> sort -> group -> paginate)
Headers, Rows, Cells - renderable units
Critical: Data & Column Stability
// WRONG - new references every render, causes infinite loops
const table = useReactTable({
  data: fetchedData.results,     // new ref!
  columns: [{ accessorKey: 'name' }], // new ref!
})

// CORRECT - stable references
const columns = useMemo(() => [...], [])
const data = useMemo(() => fetchedData?.results ?? [], [fetchedData])

const table = useReactTable({ data, columns, getCoreRowModel: getCoreRowModel() })

Column Definitions
Using createColumnHelper (Recommended)
import { createColumnHelper } from '@tanstack/react-table'

type Person = {
  firstName: string
  lastName: string
  age: number
  status: 'active' | 'inactive'
}

const columnHelper = createColumnHelper<Person>()

const columns = [
  // Accessor column (data column)
  columnHelper.accessor('firstName', {
    header: 'First Name',
    cell: info => info.getValue(),
    footer: info => info.column.id,
  }),

  // Accessor with function
  columnHelper.accessor(row => row.lastName, {
    id: 'lastName', // required with accessorFn
    header: () => <span>Last Name</span>,
    cell: info => <i>{info.getValue()}</i>,
  }),

  // Display column (no data, custom rendering)
  columnHelper.display({
    id: 'actions',
    header: 'Actions',
    cell: ({ row }) => (
      <button onClick={() => deleteRow(row.original)}>Delete</button>
    ),
  }),

  // Group column (nested headers)
  columnHelper.group({
    id: 'info',
    header: 'Info',
    columns: [
      columnHelper.accessor('age', { header: 'Age' }),
      columnHelper.accessor('status', { header: 'Status' }),
    ],
  }),
]

Column Options
Option	Type	Description
id	string	Unique identifier (auto-derived from accessorKey)
accessorKey	string	Dot-notation path to row data
accessorFn	(row) => any	Custom accessor function
header	string | (context) => ReactNode	Header renderer
cell	(context) => ReactNode	Cell renderer
footer	(context) => ReactNode	Footer renderer
size	number	Default width (default: 150)
minSize	number	Min width (default: 20)
maxSize	number	Max width
enableSorting	boolean	Enable sorting
sortingFn	string | SortingFn	Sort function
enableFiltering	boolean	Enable filtering
filterFn	string | FilterFn	Filter function
enableGrouping	boolean	Enable grouping
aggregationFn	string | AggregationFn	Aggregation function
enableHiding	boolean	Enable visibility toggle
enableResizing	boolean	Enable resizing
enablePinning	boolean	Enable pinning
meta	any	Custom metadata
Table Instance
Creating a Table
import {
  useReactTable,
  getCoreRowModel,
  getSortedRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  flexRender,
} from '@tanstack/react-table'

function MyTable() {
  const [sorting, setSorting] = useState<SortingState>([])
  const [columnFilters, setColumnFilters] = useState<ColumnFiltersState>([])
  const [pagination, setPagination] = useState<PaginationState>({
    pageIndex: 0,
    pageSize: 10,
  })

  const table = useReactTable({
    data,
    columns,
    state: { sorting, columnFilters, pagination },
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    onPaginationChange: setPagination,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
  })

  return (
    <table>
      <thead>
        {table.getHeaderGroups().map(headerGroup => (
          <tr key={headerGroup.id}>
            {headerGroup.headers.map(header => (
              <th key={header.id} onClick={header.column.getToggleSortingHandler()}>
                {header.isPlaceholder ? null :
                  flexRender(header.column.columnDef.header, header.getContext())}
                {{ asc: ' ↑', desc: ' ↓' }[header.column.getIsSorted() as string] ?? null}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody>
        {table.getRowModel().rows.map(row => (
          <tr key={row.id}>
            {row.getVisibleCells().map(cell => (
              <td key={cell.id}>
                {flexRender(cell.column.columnDef.cell, cell.getContext())}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  )
}

Sorting
const table = useReactTable({
  state: { sorting },
  onSortingChange: setSorting,
  getSortedRowModel: getSortedRowModel(),
  enableSorting: true,
  enableMultiSort: true,
  // manualSorting: true,  // For server-side sorting
})

// Built-in sort functions: 'alphanumeric', 'text', 'datetime', 'basic'
// Column-level: sortingFn: 'alphanumeric'

Filtering
Column Filtering
const table = useReactTable({
  state: { columnFilters },
  onColumnFiltersChange: setColumnFilters,
  getFilteredRowModel: getFilteredRowModel(),
  getFacetedRowModel: getFacetedRowModel(),
  getFacetedUniqueValues: getFacetedUniqueValues(),
  getFacetedMinMaxValues: getFacetedMinMaxValues(),
})

// Built-in: 'includesString', 'equalsString', 'arrIncludes', 'inNumberRange', etc.

// Filter UI
function Filter({ column }) {
  return (
    <input
      value={(column.getFilterValue() ?? '') as string}
      onChange={e => column.setFilterValue(e.target.value)}
      placeholder={`Filter... (${column.getFacetedUniqueValues()?.size})`}
    />
  )
}

Global Filtering
const [globalFilter, setGlobalFilter] = useState('')

const table = useReactTable({
  state: { globalFilter },
  onGlobalFilterChange: setGlobalFilter,
  globalFilterFn: 'includesString',
  getFilteredRowModel: getFilteredRowModel(),
})

Fuzzy Filtering
import { rankItem } from '@tanstack/match-sorter-utils'

const fuzzyFilter: FilterFn<any> = (row, columnId, value, addMeta) => {
  const itemRank = rankItem(row.getValue(columnId), value)
  addMeta({ itemRank })
  return itemRank.passed
}

const table = useReactTable({
  filterFns: { fuzzy: fuzzyFilter },
  globalFilterFn: 'fuzzy',
})

Pagination
const table = useReactTable({
  state: { pagination },
  onPaginationChange: setPagination,
  getPaginationRowModel: getPaginationRowModel(),
  // For server-side:
  // manualPagination: true,
  // pageCount: serverPageCount,
})

// Navigation
table.nextPage()
table.previousPage()
table.firstPage()
table.lastPage()
table.setPageSize(20)
table.getCanNextPage()     // boolean
table.getCanPreviousPage() // boolean
table.getPageCount()       // total pages

Row Selection
const [rowSelection, setRowSelection] = useState<RowSelectionState>({})

const table = useReactTable({
  state: { rowSelection },
  onRowSelectionChange: setRowSelection,
  enableRowSelection: true,
  enableMultiRowSelection: true,
})

// Checkbox column
columnHelper.display({
  id: 'select',
  header: ({ table }) => (
    <input
      type="checkbox"
      checked={table.getIsAllRowsSelected()}
      onChange={table.getToggleAllRowsSelectedHandler()}
    />
  ),
  cell: ({ row }) => (
    <input
      type="checkbox"
      checked={row.getIsSelected()}
      disabled={!row.getCanSelect()}
      onChange={row.getToggleSelectedHandler()}
    />
  ),
})

// Get selected rows
table.getSelectedRowModel().rows

Column Visibility
const [columnVisibility, setColumnVisibility] = useState<VisibilityState>({})

const table = useReactTable({
  state: { columnVisibility },
  onColumnVisibilityChange: setColumnVisibility,
})

// Toggle UI
{table.getAllLeafColumns().map(column => (
  <label key={column.id}>
    <input
      type="checkbox"
      checked={column.getIsVisible()}
      onChange={column.getToggleVisibilityHandler()}
    />
    {column.id}
  </label>
))}

Column Pinning
const [columnPinning, setColumnPinning] = useState<ColumnPinningState>({
  left: ['select', 'name'],
  right: ['actions'],
})

const table = useReactTable({
  state: { columnPinning },
  onColumnPinningChange: setColumnPinning,
  enableColumnPinning: true,
})

// Render pinned sections separately
row.getLeftVisibleCells()   // Left-pinned
row.getCenterVisibleCells() // Unpinned
row.getRightVisibleCells()  // Right-pinned

Column Resizing
const table = useReactTable({
  enableColumnResizing: true,
  columnResizeMode: 'onChange', // 'onChange' | 'onEnd'
  defaultColumn: { size: 150, minSize: 50, maxSize: 500 },
})

// Resize handle in header
<div
  onMouseDown={header.getResizeHandler()}
  onTouchStart={header.getResizeHandler()}
  className={`resizer ${header.column.getIsResizing() ? 'isResizing' : ''}`}
/>

Grouping & Aggregation
const [grouping, setGrouping] = useState<GroupingState>([])

const table = useReactTable({
  state: { grouping },
  onGroupingChange: setGrouping,
  getGroupedRowModel: getGroupedRowModel(),
  getExpandedRowModel: getExpandedRowModel(),
})

// Built-in aggregation: 'sum', 'min', 'max', 'mean', 'median', 'count', 'unique', 'uniqueCount'
columnHelper.accessor('amount', {
  aggregationFn: 'sum',
  aggregatedCell: ({ getValue }) => `Total: ${getValue()}`,
})

Row Expanding
const [expanded, setExpanded] = useState<ExpandedState>({})

const table = useReactTable({
  state: { expanded },
  onExpandedChange: setExpanded,
  getExpandedRowModel: getExpandedRowModel(),
  getSubRows: (row) => row.subRows, // For hierarchical data
})

// Expand toggle
<button onClick={row.getToggleExpandedHandler()}>
  {row.getIsExpanded() ? '−' : '+'}
</button>

// Detail row pattern
{row.getIsExpanded() && (
  <tr>
    <td colSpan={columns.length}>
      <DetailComponent data={row.original} />
    </td>
  </tr>
)}

Virtualization Integration
import { useVirtualizer } from '@tanstack/react-virtual'

function VirtualizedTable() {
  const table = useReactTable({ /* ... */ })
  const { rows } = table.getRowModel()
  const parentRef = useRef<HTMLDivElement>(null)

  const virtualizer = useVirtualizer({
    count: rows.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 35,
    overscan: 10,
  })

  return (
    <div ref={parentRef} style={{ height: '600px', overflow: 'auto' }}>
      <table>
        <tbody style={{ height: `${virtualizer.getTotalSize()}px`, position: 'relative' }}>
          {virtualizer.getVirtualItems().map(virtualRow => {
            const row = rows[virtualRow.index]
            return (
              <tr
                key={row.id}
                style={{
                  position: 'absolute',
                  transform: `translateY(${virtualRow.start}px)`,
                  height: `${virtualRow.size}px`,
                }}
              >
                {row.getVisibleCells().map(cell => (
                  <td key={cell.id}>
                    {flexRender(cell.column.columnDef.cell, cell.getContext())}
                  </td>
                ))}
              </tr>
            )
          })}
        </tbody>
      </table>
    </div>
  )
}

Server-Side Operations
const table = useReactTable({
  data: serverData,
  columns,
  manualSorting: true,
  manualFiltering: true,
  manualPagination: true,
  pageCount: serverPageCount,
  state: { sorting, columnFilters, pagination },
  onSortingChange: setSorting,
  onColumnFiltersChange: setColumnFilters,
  onPaginationChange: setPagination,
  getCoreRowModel: getCoreRowModel(),
  // Do NOT include getSortedRowModel, getFilteredRowModel, getPaginationRowModel
})

// Fetch data based on state
useEffect(() => {
  fetchData({ sorting, filters: columnFilters, pagination })
}, [sorting, columnFilters, pagination])

TypeScript Patterns
Extending Column Meta
declare module '@tanstack/react-table' {
  interface ColumnMeta<TData extends RowData, TValue> {
    filterVariant?: 'text' | 'range' | 'select'
    align?: 'left' | 'center' | 'right'
  }
}

Custom Filter/Sort Function Registration
declare module '@tanstack/react-table' {
  interface FilterFns {
    fuzzy: FilterFn<unknown>
  }
  interface SortingFns {
    myCustomSort: SortingFn<unknown>
  }
}

Editable Cells via Table Meta
declare module '@tanstack/react-table' {
  interface TableMeta<TData extends RowData> {
    updateData: (rowIndex: number, columnId: string, value: unknown) => void
  }
}

const table = useReactTable({
  meta: {
    updateData: (rowIndex, columnId, value) => {
      setData(old => old.map((row, i) =>
        i === rowIndex ? { ...row, [columnId]: value } : row
      ))
    },
  },
})

Key Imports
import {
  createColumnHelper, flexRender, useReactTable,
  getCoreRowModel, getSortedRowModel, getFilteredRowModel,
  getPaginationRowModel, getGroupedRowModel, getExpandedRowModel,
  getFacetedRowModel, getFacetedUniqueValues, getFacetedMinMaxValues,
} from '@tanstack/react-table'

import type {
  ColumnDef, SortingState, ColumnFiltersState, VisibilityState,
  PaginationState, ExpandedState, RowSelectionState, GroupingState,
  ColumnOrderState, ColumnPinningState, FilterFn, SortingFn,
} from '@tanstack/react-table'

Best Practices
Always memoize data and columns to prevent infinite re-renders
Use flexRender for all header/cell/footer rendering
Use table.getRowModel().rows for final rendered rows (not getCoreRowModel)
Import only needed row models - each adds processing to the pipeline
Use getRowId for stable row keys when data has unique IDs
Use manualX options for server-side operations
Pair controlled state with both state.X and onXChange
Use module augmentation for custom meta, filter fns, sort fns
Use column helper for type-safe column definitions
Set autoResetPageIndex: true when filtering should reset pagination
Common Pitfalls
Defining columns inline (creates new ref each render)
Forgetting getCoreRowModel() (required for all tables)
Using row models without importing them
Not providing id when using accessorFn
Mixing manualPagination with client-side getPaginationRowModel
Forgetting colSpan for grouped headers
Not handling header.isPlaceholder for group column spacers
Weekly Installs
1.1K
Repository
tanstack-skills…k-skills
GitHub Stars
14
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass