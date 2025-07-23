# React Client Folder Structure Guide

This document serves as a guide for developers working on the Task Management React application. It outlines the purpose of each folder and provides guidelines for where to add new features or modifications.

## `/src` Directory Structure

```
src/
├── App.css                 # Main application styles
├── App.tsx                 # Root application component
├── index.css               # Global CSS styles
├── main.tsx                # Application entry point
├── vite-env.d.ts           # Vite environment type definitions
├── assets/                 # Static assets (images, icons, etc.)
├── components/             # Reusable UI components
├── constants/              # Application constants and configuration
├── contexts/               # React Context providers
├── hooks/                  # Custom React hooks
├── layouts/                # Layout components
├── pages/                  # Page components (route components)
├── services/               # API services and external integrations
├── skeletons/              # Loading skeleton components
├── styles/                 # Additional styling files
├── types/                  # TypeScript type definitions
└── utils/                  # Utility functions and helpers
```

## Detailed Folder Descriptions

### 📁 `assets/`

**Purpose**: Store static assets like images, icons, logos, and other media files.
**When to use**:

- Adding new images or icons
- Logo files
- Static media content

**Example structure**:

```
assets/
├── images/
├── icons/
├── logos/
└── react.svg
```

### 📁 `components/`

**Purpose**: Reusable UI components that can be used across different pages.
**When to use**:

- Creating reusable buttons, forms, modals
- Building component libraries
- Shared UI elements

**Current structure**:

```
components/
├── Button.tsx              # Reusable button component
├── admin/                  # Admin-specific components
└── guest/                  # Guest-specific components
```

**Guidelines**:

- Use PascalCase for component names
- Each component should have its own file
- Group related components in subdirectories
- Consider creating an `index.ts` for easier imports

### 📁 `constants/`

**Purpose**: Store application-wide constants, configuration values, and static data.
**When to use**:

- API endpoints
- Configuration values
- Menu items
- Static lists or mappings

**Current files**:

- `navbar.ts` - Navigation-related constants

### 📁 `contexts/`

**Purpose**: React Context providers for global state management.
**When to use**:

- User authentication state
- Theme management
- Global application state
- Shopping cart state

**Current files**:

- `useAuthContext.tsx` - Authentication context

### 📁 `hooks/`

**Purpose**: Custom React hooks for reusable logic.
**When to use**:

- API data fetching logic
- Form handling
- Local storage management
- Complex state logic

**Current files**:

- `useAuth.tsx` - Authentication hook

**Guidelines**:

- Start hook names with "use"
- Keep hooks focused on single responsibilities
- Document hook parameters and return values

### 📁 `layouts/`

**Purpose**: Layout components that define the structure of pages.
**When to use**:

- Page layouts with headers, sidebars, footers
- Different layouts for different user roles
- Responsive layout components

**Current structure**:

```
layouts/
├── Footer.tsx              # Application footer
├── Sidebar.tsx             # Main sidebar component
├── admin/
│   └── AdminLayout.tsx     # Admin-specific layout
└── guest/
    ├── GuestLayout.tsx     # Guest layout
    └── GuestSidebar.tsx    # Guest sidebar
```

### 📁 `pages/`

**Purpose**: Page components that represent different routes in the application.
**When to use**:

- Creating new pages/routes
- Route-specific components
- Page-level logic and state

**Current structure**:

```
pages/
├── Homepage.tsx            # Main homepage
├── admin/
│   └── AdminHomepage.tsx   # Admin dashboard
└── guest/
    └── GuestHomepage.tsx   # Guest homepage
```

**Guidelines**:

- One component per route
- Use descriptive names ending with "Page" or similar
- Group pages by user role or feature area

### 📁 `services/`

**Purpose**: API services, external integrations, and data fetching logic.
**When to use**:

- API calls and HTTP requests
- Third-party service integrations
- Data transformation logic

**Current files**:

- `_axios.ts` - Axios configuration
- `Chat.ts` - Chat service implementation

### 📁 `skeletons/`

**Purpose**: Loading skeleton components for better UX during data loading.
**When to use**:

- Creating loading states
- Placeholder components while content loads
- Improving perceived performance

### 📁 `styles/`

**Purpose**: Additional styling files, themes, and CSS modules.
**When to use**:

- Theme definitions
- CSS modules
- SCSS/Sass files
- Style utilities

### 📁 `types/`

**Purpose**: TypeScript type definitions and interfaces.
**When to use**:

- Defining data models
- API response types
- Component prop types
- Global type definitions

**Guidelines**:

- Use descriptive names for types
- Group related types in the same file
- Export types for reusability

### 📁 `utils/`

**Purpose**: Utility functions and helper methods.
**When to use**:

- Data formatting functions
- Validation helpers
- Common algorithms
- Pure functions

**Current files**:

- `formatters.ts` - Data formatting utilities

## Best Practices

### File Naming Conventions

- **Components**: PascalCase (e.g., `UserProfile.tsx`)
- **Hooks**: camelCase starting with "use" (e.g., `useLocalStorage.ts`)
- **Utilities**: camelCase (e.g., `formatDate.ts`)
- **Constants**: camelCase or UPPER_SNAKE_CASE (e.g., `apiEndpoints.ts`)

### Organization Tips

1. **Group by Feature**: Consider organizing by feature rather than file type for larger applications
2. **Index Files**: Use `index.ts` files for cleaner imports
3. **Co-location**: Keep related files close together
4. **Barrel Exports**: Use barrel exports for better import organization

### Adding New Features

1. **Identify the Type**: Determine if it's a component, page, service, etc.
2. **Check Existing Patterns**: Follow existing naming and organization patterns
3. **Consider Reusability**: Place reusable code in appropriate shared folders
4. **Update Documentation**: Update this file when adding new patterns or folders

## Role-Based Organization

The current structure supports role-based access with separate folders for:

- **Admin**: Administrative features and components
- **Guest**: Public/guest user features
- **Shared**: Common components and utilities

When adding new features, consider which user role they serve and place them in the appropriate subfolder.
