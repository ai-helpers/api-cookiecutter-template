# Contributing

This document describes the motivations and steps for contributing to this repository.

- [Contributing](#contributing)
  - [Why should I contribute](#why-should-i-contribute)
    - [Motivations](#motivations)
    - [Collaboration](#collaboration)
  - [How to contribute](#how-to-contribute)
    - [Explain a problem](#explain-a-problem)
    - [Provide a code solution](#provide-a-code-solution)
  - [How to publish](#how-to-publish)
    - [Approval process](#approval-process)
    - [Release process](#release-process)

## Why should I contribute

This section explains the reasons to contribute and the collaboration between actors.

### Motivations

1. Introduce new features beneficial to you and other users.
2. Fix an issue that impacts negatively your work or the work of others.
3. Provide better practices to improve the robustness and efficiency of the code base.
4. Increase the code base performance to speed-up the execution and consume less resources.
5. Write clearer and more complete documentation to improve the comprehension and usage for end users.

### Collaboration

The collaboration process happens between **end users** and **repository owners**.

**End users** can [explain a problem](#explain-a-problem) and [provide a code solution](#provide-a-code-solution) as their main contribution.

**Repository owners** are mainly and solely responsible for both the [approval](#approval-process) and [release](#release-process) process.

## How to contribute

This section details the steps to contribute to this repository using [issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) and [pull requests (PR)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

### Explain a problem

The first step of the collaboration process is to write a [GitHub issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) to describe the problem to others.

This allows the repository users and owners to discuss options and find the best approach to solve the problem.

You can refer to [GitHub documentation on creating an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue) to explain a problem with advanced structure and markup.

### Provide a code solution

You can solve an issue documented in this repository by writing some code and creating a [Pull Request (PR)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

A pull request is required to isolate and review the proposed changes as part of the [approval process](#approval-process).

You can quickstart the development of the repository by following the instruction in `README.md`.

## How to publish

This section defines the approval and release processes for merging contributions to this repository.

### Approval process

The approval process is the responsability of the **repository owners**. There are 3 requirements:

1. The contribution provides added value to the organization
2. [The technical status checks pass before merging the pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)
3. [The contribution receives the approval of at least one repository owners](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews)

If the requirements are met, the **repository owners** can [accept and merge the pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews) to the main branch.

### Release process

To provide a consistent evolution of the repository to end users, contributions are grouped into **versionned releases**.

During development, the repository owners address several issues in a [milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones) to report their progress.

Once a milestone is complete, the repository owners can publish a new [tag](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/managing-commits/managing-tags) and [a release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).