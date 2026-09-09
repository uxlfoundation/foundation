============
UXL Meetings
============

Attending a Meeting
===================

Meetings are hosted in Zoom.

You can see meeting information in 2 places. Both places have Zoom links.

`My Meetings`_ in openprofile.
  All the meetings for groups that I have joined.

Group specific pages in lists.uxlfoundation.org
  All the meetings for a specific group. Visit `UXL Groups`_, select a group
  that you have joined, and then click on Calendar in the left column. For
  example, see `Open Source WG Calendar`_.


Hosting a Meeting
=================

Linux foundation infrastructure to support meeting hosts:

* Zoom
* Automatic calendar reminders
* Calendar to publish a meeting schedule


Sending a Meeting Announcement
------------------------------

Publish an agenda in advance of the meeting. This is a good practice for
several reasons:

* People can prepare for the meeting
* People can decide if they want to attend the meeting and potentially invite
  others

Send the agenda to the group mailing list linked from its repository page.
Include the meeting date, time zone, agenda topics and the calendar link.
Coordinate calendar or host changes with the group chairs or foundation operations.

Recording a Meeting
-------------------

There are many benefits to recording a meeting

* People who cannot attend can watch the recording later.
* People who attended can review the recording to refresh their memory and
  share the meeting with others
* Transcripts will be available. It is much quicker to view a transcript than
  to watch a recording. You can find the information you need much faster.
  There are also tools for summarizing meeting transcripts. This is useful for
  the note taker as well as attendees.

Check the recording access settings with the host before the meeting and tell
attendees that it is being recorded. Recordings may require membership and an
openprofile account; do not assume that every recording is publicly accessible.
Do not include private information in a public meeting record.

There are two ways to record a meeting:

* Automatically record the meeting. This is the simplest way to record a
  meeting. The recording will be available after the meeting ends in `My
  Meetings`_.

* Manually record the meeting. Manual recording will give you more control
  over the recording. In practice, I have found this very difficult and do not
  recommend the option.

  * You will forget to record
  * You need to provide a key to authenticate as meeting host and then turn on
    recording. It is a distraction.
  * If the regular host is not present, the person covering will not remember
    to record, or not have the key, or not know how to use the key to record.
  * Automatic and manual recordings are available in different places. I have
    not found the manual recording after the meeting ends.

Publishing Meeting Minutes
--------------------------

Use the meeting-notes template linked from CONTRIBUTING.md. Save new notes with
a YYYY-MM-DD filename in the relevant group directory and add them to its index.
Include decisions, action owners, presentation links and recording access details.
Submit a pull request for review by the relevant group chairs before publication.
Preserve existing filenames and historical records when correcting links.
For new large recordings, link to an approved stable video host rather than
committing the video file to Git.

.. _`UXL Groups`: https://lists.uxlfoundation.org/groups
.. _`Open Source WG Calendar`: https://lists.uxlfoundation.org/g/open-source-wg/calendar#
.. _`My Meetings`: https://openprofile.dev/my-meetings
