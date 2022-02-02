# CP13 Group 1/5 Frontend Integration Development Guide

## Introduction

This guide sets out the development guideline, best practice, and things of note for integration effort of the survey
builder (by g1) and account+response system (by g5) codebases.

This project runs on the stable Vue v2.x. Do not refer to guides using Vue v3.x for compatibility reasons. A vue cheatsheet for your reference: https://www.vuemastery.com/pdf/Vue-Essentials-Cheat-Sheet.pdf

## Commands

Prerequisite: Install npm dependencies
```sh
npm install
```
To build the project for deployment
```sh
npm run build
```
To run the project in dev mode
```sh
npm run dev
```

## Skeleton
The frontend codebase is written using JavaScript framework Vue. This Vue project is located under the `./cp13` directory. In the project, there are the following sections:
- node_nodules: generated by running `npm install` and stores npm dependencies required for this project. This directory is not a part of the codebase and **SHOULD NOT** be committed to the repository.
- public: stores static assets, https://cli.vuejs.org/guide/html-and-static-assets.html
- src: project source
- tests: test suites

Under the source directory, there are the following directory:
- components: reusable interface components
- locales: localisation
- router: URL routing definition
- services: various JavaScript logic
- store: Vuex store management
- views: interface pages
- App.vue: the base view

## Views
Vue paradigm focuses the use of views, which defines a particular unit of the interface. Each view has its own HTML, CSS, and JavaScript definition. They can be re-ued and nested to form more complex structures and hierarchies.

`App.vue` is the base view of the project and is rendered for every page. Different contents/views are inserted to `App.vue`, depending on factors such as routing and other defined logic.

### Basic View
Read this documentation: https://vuejs.org/v2/guide/components.html

A basic view looks like this:
```html
<script>
export default {
}
</script>

<template>
  <div id="something">
  </div>
</template>

<style scoped>
</style>
```
#### View Behaviour
The JavaScript code inside `<script>` tag defines the behaviour of the view. It is wrapped inside a function called `export default`, and you can define various aspects of the view behaviour by modifying the object inside `export default`. Some notable ones:
- `components: {obj}`, defines components that can be used in the template
- `props: {obj}`, defines the argument the template takes (e.g. a button template might take an argument that defines the btn text), https://vuejs.org/v2/guide/components-props.html
- `data: {function}`: defines variables (e.g. first name and last name)
- `computed: {obj}`: defines derived values (e.g. full name), https://vuejs.org/v2/guide/computed.html
- `methodsL: {obj}`: defines custom javascript methods

#### View Layout
The layout is defined inside `<template>`, which consists of regular HTML with Vue-specific directives to conditionally and dynamically manipulate the layout (e.g. built-in conditional and loops). **Do NOT** use vanilla JS to retrieve or change the content of HTML. Refer to the following documentation to learn more:
- HTML Classes: https://vuejs.org/v2/guide/class-and-style.html
- Conditional: https://vuejs.org/v2/guide/conditional.html
- Loops: https://vuejs.org/v2/guide/list.html
- Event Handling: https://vuejs.org/v2/guide/events.html
- Form input: https://vuejs.org/v2/guide/forms.html

#### View Styling
Styling is defined inside `<style scoped>` which consists of CSS code. CSS definition inside the tag are only effective to the current scope (i.e. the view itself). There also exists `<style>` that gets applied globally. **DO NOT** use `<style>` for any view other than `App.vue` and only put CSS definition under `<style>` if it is intended to be applied globally for all views.

In most cases, use `<style scoped>`.

### Components and Pages
If some HTML layout (and its accompanying CSS and JavaScript definitions/behaviour) are to be used multiple times in the project, you **MUST** create a view and put it in under `./components`. That should include things like buttons, tabs, cards, and etc.

If a view is in `./views`, it should match a definition in the router. In other words, A view in `./views` deals with the layout, styling, and behaviour of individual web pages which are distinguished by different URL. For example, there exists `index.vue` which is accessed by `/`, and `SurveyBuilder.vue` which is accessed by `/build-survey`.

## State Management
https://vuex.vuejs.org/#what-is-a-state-management-pattern

There exists a library called Vuex that centralises variables/states for all components. Data should be stored using Vuex if it is shared between views (e.g. current user token). You **MUST** use Vuex for data shared between views.

Vuex data is not persistent, use it in conjunction with local storage for persistent states.