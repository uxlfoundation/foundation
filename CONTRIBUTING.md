# Contributing

Use this repository for foundation governance, SIG documentation and community infrastructure.
Use the [Working Group](https://github.com/uxlfoundation/open-source-working-group)
for cross-project work packages, and the relevant library repository for implementation bugs.

## Issues and work packages

Use an issue template to describe the problem, affected area, evidence and
completion criteria. Identify an owner when one has agreed to take the work.
Maintainers use `needs-triage` for items awaiting a decision and area labels for
routing. An old issue is not automatically obsolete: close it only with evidence
of completion, a duplicate reference or an explicit decision not to pursue it.
Reassign an open issue out of a closed milestone when agreeing its next target.

## Documentation and meeting notes

Make focused pull requests and explain what changed and how it was checked.
Use the [meeting-notes template](.github/meeting-notes-template.rst) for new notes.
Use YYYY-MM-DD in new filenames, update the relevant index, and check relative
links and presentation attachments. Preserve existing filenames and historical
decisions; correct broken links without rewriting the meeting's conclusions.
Link new large recordings from an approved stable host rather than adding video
binaries. State any membership requirement for recording access.

Run `python .github/scripts/check_local_links.py` from the repository root.
The check validates local file targets in Markdown and reStructuredText; it does
not check external websites or section anchors. Public links and meeting content
also need a human review.

## Review and repository maintenance

The existing `@uxlfoundation/sig-leaders` team routes repository reviews through
CODEOWNERS. Changes to meeting decisions or leadership need the relevant chairs'
confirmation. Prefer one approving review and passing documentation checks before
merging; keep proposed changes separate from approved decisions. Administrators
retain an exception path for urgent maintenance and should document any exception
in the PR. Do not treat an automated link check as approval of meeting content.

Use the existing foundation and project policies. This guide does not introduce
a new license or change governance or contribution terms. Ask foundation
operations to confirm applicable terms before importing third-party material.
Report security vulnerabilities through the affected project's private reporting
channel or security policy, rather than posting details in a public issue.

For rendering and meeting-index checks, install `docutils==0.19` and run
`python .github/scripts/check_document_structure.py`. The check reports malformed
reStructuredText and dated records missing from sibling indexes. External URLs
and cross-document section anchors still require review.

Maintainers can run **External link review** from the Actions tab to obtain an
advisory report for guidance and indexes. It distinguishes missing pages from
access restrictions and transient failures, and does not block pull requests.
PDFs and restricted meeting materials are excluded. To run locally, use
`python .github/scripts/report_external_links.py`; it writes `external-link-report.md`.
