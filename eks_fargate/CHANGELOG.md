# CHANGELOG - eks_fargate

## 2.1.0 / 2021-10-04

* [Added] Add runtime configuration validation. See [#8910](https://github.com/DataDog/integrations-core/pull/8910).
* [Added] Add HTTP option to control the size of streaming responses. See [#10183](https://github.com/DataDog/integrations-core/pull/10183).
* [Added] Add allow_redirect option. See [#10160](https://github.com/DataDog/integrations-core/pull/10160).
* [Fixed] Fix the description of the `allow_redirects` HTTP option. See [#10195](https://github.com/DataDog/integrations-core/pull/10195).

## 2.0.0 / 2021-04-19 / Agent 7.28.0

* [Changed] Refactor kubelet and eks_fargate checks to use `KubeletBase`. See [#8798](https://github.com/DataDog/integrations-core/pull/8798).

## 1.4.0 / 2021-03-07 / Agent 7.27.0

* [Added] Add pod capacity metrics. See [#8754](https://github.com/DataDog/integrations-core/pull/8754).
* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 1.3.0 / 2021-01-25 / Agent 7.26.0

* [Added] Add new default for newly autodiscovered checks. See [#8177](https://github.com/DataDog/integrations-core/pull/8177).

## 1.2.0 / 2020-12-11 / Agent 7.25.0

* [Added] Add config specs. See [#8004](https://github.com/DataDog/integrations-core/pull/8004).

## 1.1.1 / 2020-09-21 / Agent 7.23.0

* [Fixed] Fix style for the latest release of Black. See [#7438](https://github.com/DataDog/integrations-core/pull/7438).

## 1.1.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 1.0.0 / 2020-02-22 / Agent 7.18.0

* [Added] Introducing the eks_fargate check. See [#5417](https://github.com/DataDog/integrations-core/pull/5417).
