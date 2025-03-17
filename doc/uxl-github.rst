=================
UXL use of GitHub
=================

This document describes the use of GitHub for the UXL project.

uxlfoundation org
=================

The UXL project is hosted on GitHub under the `uxlfoundation`_ organization. It
contains repos that are not specific to any one open source project. There will
be a small set of ``owners`` for the org. ``@thelinuxfoundation`` is an owner
as backup in case UXL owners are not available.

Giving Access to Resources
--------------------------

Try to use GitHub Teams that are defined by roles. For example,
``@oneapi-spec-maintainers`` are the maintainers for the oneapi spec and have
write access. Using a team-based role instead of directly adding maintainers to
the repo makes it possible to ``@tag`` the team in issues and PRs.

If a role specific team is overkill, but you still want to be able to ``@tag``
someone in a repo in uxlfoundation org, they can be added to the `UXL Members`_
team. If you have a role in UXL (e.g. SIG leader), you can be added as a
maintainer of this team.

GitHub Actions
==============

UXL Foundation projects make use of GitHub Actions for continuous integration
and testing.

Available Runners
-----------------

In addition to the `Standard GitHub-hosted runners`_ the UXL Foundation GitHub
organization has several member-hosted test systems available for use:

Intel Data Center GPU Max 1550
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These systems are provided by Intel and maintained by Codeplay Software Ltd.

The following labels are usable:

- label: uxl-xlarge
    - specs: 4 vCPU, 16Gi, No GPU
- label: uxl-gpu-xlarge
    - specs: 4 vCPU, 16Gi, 1x 1550 GPU
- label: uxl-gpu-2xlarge
    - specs: 8 vCPU, 32Gi, 2x 1550 GPU
- label: uxl-gpu-4xlarge
    - specs: 16 vCPU, 64Gi, 1x 1550 GPU
- label: uxl-gpu-6xlarge
    - specs: 24 vCPU, 96Gi, 2x 1550 GPU
- label: uxl-gpu-8xlarge
    - specs: 32 vCPU, 128Gi, 1x 1550 GPU
- label: uxl-gpu-10xlarge
    - specs: 40 vCPU, 160Gi, 2x 1550 GPU
- label: uxl-gpu-12xlarge
    - specs: 48 vCPU, 192Gi, 4x 1550 GPU
- label: uxl-gpu-16xlarge
    - specs: 64 vCPU, 256Gi, 1x 1550 GPU
- label: uxl-gpu-24xlarge
    - specs: 96 vCPU, 384Gi, 4x 1550 GPU
- label: uxl-gpu-48xlarge
    - specs: 170 vCPU, 769Gi, 8x 1550 GPU


.. _`uxlfoundation`: https://github.com/uxlfoundation
.. _`UXL Members`: https://github.com/orgs/uxlfoundation/teams/uxl-members
.. _`Standard GitHub-hosted runners`: https://docs.github.com/en/enterprise-cloud@latest/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#choosing-github-hosted-runners
