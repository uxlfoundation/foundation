================
UXL Use of Slack
================

This document describes the use of Slack for the UXL project.

Channels
========

There are channels for each SIG (e.g. ``sig-math``), project (e.g. ``onemkl``), and working group (e.g. ``wg-open-source``). Channels are public unless there is a specific need (e.g. ``steering-committee``, ``security``).

GitHub Integration
==================

It is possible for GitHub Actions to post messages in Slack. This can be useful for notifications of CI failures, new issues, etc. To enable this feature for a channel:

* add `@GitHub Messages` to the channel
* add a GitHub action to your repo. See `Slack Action`_ as an example.
* add ``SLACK_BOT_TOKEN`` to the GitHub secrets for the repo. Get the value
  from Robert Cohn

Getting the Token
=================

The token is connected with a slack app. You need to be signed in to uxlfoundation workspace to see it, otherwise you will not see the app.

.. _`Slack Action`: https://github.com/uxlfoundation/spec-working-group/blob/main/.github/workflows/slack-pr.yaml
