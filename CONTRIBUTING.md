# Contributing code

The following steps help our team to stay coordinated:

1. Open/assign an issue to yourself.
2. Immediately open a pull request by comparing your branch against the `develop` branch
2. Label your pull request as `WIP`, so that other developers can see the work in progress
3. When ready for review, @mention the development team, so that we know to review your code

## Using Git Flow

1. Checkout the repository
1. Install [gitflow](https://github.com/nvie/gitflow/wiki/Installation)
2. git checkout master
3. <code>git flow init</code> and follow:

```
Which branch should be used for bringing forth production releases?
   - develop
   - master
Branch name for production releases: [master]

Which branch should be used for integration of the "next release"?
   - develop
Branch name for "next release" development: [develop]

How to name your supporting branch prefixes?
Feature branches? [feature/]
Release branches? [release/]
Hotfix branches? [hotfix/]
Support branches? [support/]
Version tag prefix? []
```

## If you choose not to use Git Flow

When contributing code, please follow the [Gitflow guidelines](http://danielkummer.github.io/git-flow-cheatsheet/). Specifically:

1. Create a new feature branch from the `develop` branch
2. Prefix your feature branch name with `feature`

