UXL use of Slack
==================

Slack supports discussion among projects, Special Interest Groups and the
Working Group. Find participation routes on the `foundation home <../README.md>`__.
Use the workspace's channel directory to find a project or group; channel names
may differ from repository names.

Channels and access
---------------------

The Working Group uses ``wg-open-source``. Ask group chairs or workspace
administrators about other channels and access. Keep membership-restricted
discussions and credentials in the appropriate private channels.

GitHub notifications
----------------------

The Working Group's `Slack notification workflow
<https://github.com/uxlfoundation/open-source-working-group/blob/main/.github/workflows/slack-pr.yaml>`__
notifies its channel when an RFC label is added and when a pull request labelled
``meeting notes`` is merged.

To request a similar integration:

* Identify the destination channel and the events that should produce messages.
* Coordinate app access with workspace administrators and workflow configuration
  with repository maintainers.
* Arrange the repository secret through the administrators. The existing workflow
  uses ``SLACK_BOT_TOKEN``; do not publish its value in issues or documentation.
* Check delivery with the administrators and document the support role.

The current app owner and access-request contact are not documented here.
Confirm them with workspace administrators before changing the integration.

`Community operations <README.rst>`__
