# Filing an academic integrity case

Without waiting until the end of the term

**Note:** This document does not represent any changes in policy. Instead, its intent is to clearly state existing policy in an approachable manner.

## Change Log

* Sep 25, 2024: Initial circulation date

A fully detailed changelog can be found here:
[here](https://github.com/inducer/uiuc-academic-integrity/commits/main/doc/filing-a-case.md).

## About this Document

Read the [Provost's Quick Reference Guide](https://provost.illinois.edu/policies/policies/academic-integrity/instructors-quick-reference-guide-to-academic-integrity/) (just \~900 words) on academic integrity. The rest of this document assumes that you know those basics and provides concrete implementation advice.

## How does a case proceed? (i.e. timeline)

* You file an allegation on FAIR. This is the notification date (“D”).
  * Make a good-faith effort to account for all work submitted by D by the student and include any infractions found in the allegation.
* The student responds, also on FAIR (no later than D \+ 10 business days)
* You file a “Finding”, also on FAIR.
  * **Recommended**: no later than D \+ 20 business days
  * **Hard deadline: (later of D and grade entry deadline) \+ 20 business days**
  * **Last opportunity to account for infractions on or before D** by amending the allegation
* The student has the option to request an appeal (within 5 business days after you file your finding).
* An appeal hearing occurs (appeal request from student \+ 20 business days).

D **does not change** even if the case reverts to an earlier step in the process for any reason.

## Guidelines

* Read the [Provost's Quick Reference Guide](https://provost.illinois.edu/policies/policies/academic-integrity/instructors-quick-reference-guide-to-academic-integrity/) on academic integrity.
* **Precision** in the original allegation counts. Ask yourself how the allegation could be misunderstood or unclear, especially to a student who may be an unwitting participant.
  * Effort here pays for itself many times over in later stages of the process: less arguing with the student, reduced appeal rates, …
* **Well-documented:**  Put key evidence and course policies  into the FAIR case, so that it’s clear to everyone what is being alleged.
  * Generally, there should be **no personally identifying information** in the case documentation, unless it’s already known to all parties or the student needs this information to respond to the allegation.   This means that you may need to redact this information from, e.g., PDF submissions.
  * As a specific example, please do not reveal the identity of other students whose code may be part of a plagiarism case.
* Your **audience** includes the student (who may not have done anything wrong) as well as appeals committees (which include faculty and students).
* **File early, file often.** The process works best if the granularity of one allegation is
  one separate incident, e.g. one assignment.
  * Filing late may force you to include many suspected infractions in one allegation notice.
* ***Suggested*** **sanction for first infraction:** impact of roughly 10% of the student’s final course grade, i.e. a reduction of one letter grade. The method of accounting leading to this may vary by course/type of assignment.
  * [https://cs.illinois.edu/academics/honor-code](https://cs.illinois.edu/academics/honor-code) will be updated to match this suggestion.
* ***Suggested*** **sanction for repeat infraction:** a failing grade in the course.
* During appeals hearings, it has been advantageous to have a stated policy on penalties for integrity violations in the course syllabus.

## Preventing Infractions

A few strategies can help limit opportunities for academic dishonesty:

* Rotating/routinely ‘refreshed’ assignments
* Clear policies
* Assessments in defined environments (e.g. CBTF, online proctoring)
* Enforcement of prerequisites (to ensure students have the necessary background to complete assignments, lessening the need for resorting to desperate measures)

## Detecting Infractions

There are some tools available for detecting unauthorized sharing of code among students:

* [https://github.com/cs50/compare50](https://github.com/cs50/compare50) \- Runs locally, Python. Fairly modern, reasonably approachable output. Used by some CS faculty.
* [https://github.com/blingenf/copydetect](https://github.com/blingenf/copydetect) \- Runs locally, Python. A reimplementation of the MOSS algorithm.
* [https://github.com/dodona-edu/dolos](https://github.com/dodona-edu/dolos) \- Runs locally, Javascript.
* [https://github.com/manuel-freire/ac2](https://github.com/manuel-freire/ac2) \- Runs locally, Java.
* [https://theory.stanford.edu/\~aiken/moss/](https://theory.stanford.edu/~aiken/moss/) \- Relies on an Internet-based service run, see below on potential FERPA concerns. Output is a bit clunky/old-fashioned, but has been the go-to tool for a long time.
* Don’t discount the classics\! Diff and grep can be quite helpful. (Consider diff options \--ignore-all-space, –ignore-case.)

For written assignments, there are fewer tools available. All appear to be web-based, no endorsement intended:

* [https://www.turnitin.com/](https://www.turnitin.com/)
* [https://plagiarismcheck.org/](https://plagiarismcheck.org/)
* [https://www.plagscan.com/](https://www.plagscan.com/)

TurnItIn is available via Canvas.
Be mindful of your obligations under FERPA when using external tools. You may need to remove personally identifiable information. Some tools for this include:

* On OSX, the “redact” feature in the “Preview” PDF viewer.

## Sample Wording

FAIR pre-fills most of the letter to the student. For example, for the common case of ‘unexplained code similarity’, a snippet like this may suffice:

The file ‘xyz.py’ you submitted for MP 5 has many lines identical to another student's submission. The two files are attached, as is an automated report on detected similarities.

Course policies for CS123 in the fall of 2050 can be found at https://xyz.illinois.edu/.

**Important:** When alleging similarity between the submissions of two or more students, **never** disclose the identities of the other students involved as part of the allegation.

## Good Reasons for Filing Early

Academic integrity (FAIR) cases should be filed as soon as you have good reason to believe an infraction happened.   Do not wait until the end of the term.    Four reasons for filing in a timely manner:

* Students benefit from consistency. Ramping up enforcement late in the term may lead to surprise and frustration.
* An early warning will cause many students to shape up and do future work as intended.
* The small minority who don’t listen will end up with a second case of FAIR, which is vastly more serious than a first infraction.  (Three FAIR cases often result in a suspension from the university. Two may be sufficient in the case of a graduate student.)
* You can amend your allegation if more potential infractions come to light, up until the time when you issue your finding.
* Most appeals can be heard before the term ends.
* It strains our appeals system when too many cases pile up at the end of the term, and the process gets less pleasant for everyone if the process drags out (summer travel, priorities, student availability)

In particular, we have had major problems arranging appeals from spring term that spill over into summer.   In the summer, most faculty are out of town and the rest aren’t being paid to do this kind of work.  The undergraduates are often working full-time and also technically not available.  The student code no longer allows us to just delay these appeals until the start of fall term.

## Preparing to File

If you have not filed an academic integrity case recently, first read the [Provost's Quick Reference Guide](https://provost.illinois.edu/policies/policies/academic-integrity/instructors-quick-reference-guide-to-academic-integrity/) and the relevant parts of the student code’s discussion of [academic integrity infractions](https://studentcode.illinois.edu/article1/part4/1-402/).

Take a moment to consider whether the observed behavior merits an academic integrity allegation.   Minor misdeeds, honest mistakes, and misunderstanding can be handled using standard classroom processes (e.g. deducting points, giving warnings).   Does it seem like the student was deliberately or negligently violating the academic integrity rules in a way that you consider significant?

You may communicate (e.g. email, in-person) with the student(s) before filing the allegation on FAIR, but you are not required to do so.  If you suspect an infraction has occurred, it is generally best to just proceed to allege using FAIR, without any informal communication with the student prior. This way, the student is on-the-record from the get-go. If they produce legitimate evidence that they should not be accused of an infraction, you can always acknowledge that at the finding stage and close the case.

Before you file the allegation, assemble a brief description of your evidence, enough to allow a coherent student response. Consider the following sources:

* The student submission(s)
* Third-party sources for plagiarized content
* Which parts were apparently copied? E.g. MOSS output, your notes about what similarities you found
* The text of the assignment
* Course policies on collaboration, use of third-party code, etc.
* Relevant emails and forum (e.g. piazza, chat, wiki) posts
* Submission timelines and/or history, for all involved, if collected
* If you discuss with the student prior to filing the allegation, make a brief note of the date and what you discussed. Similarly, keep notes if you observe suspicious behavior (e.g. in a case involving exam cheating).

Also browse the student’s prior work for any other infractions.

## Details of timelines

Your first step is to create a new case on the FAIR system (my.siebelschool, academic tab, academic integrity), including a clear description of what you suspect the student of having done.   This sends the initial notification to the student.  The notification date is important, so let’s call it D.

The student has now been warned.   Anything they might do or submit after D will go into a second FAIR allegation. (For homework, the relevant date is when it was submitted.)

The student has 10 business days from D to respond on FAIR.

Once the student has responded, you should thoroughly investigate their work.   This must include examining all work through date D for possible additional infractions.   If you uncover additional infractions, you must amend your allegation on FAIR.   This sends the process back to the initial allegation stage, and the student gets to file a new response, but it does not change the notification date D.

Tip:  save a copy of the student’s previous response before you file an amended allegation.   It’s possible for this to get lost if they do the wrong thing with the user interface filing their new response.

The deadline for filing your finding is 20 business days after the grade entry deadline for the course.   Obviously we’d like to see cases wrapped up much faster than that.   However, it’s important to do a thorough search for additional infractions before date D, because this will be your only chance to file a FAIR charge for them.   Delays may be unavoidable when (for example):

* Other students are still working on this assignment.
* Exams taken before D are still being graded.
* Other students have not yet responded to closely-related allegations.

Take the time required to wait out such delays and do a proper job.

In a course with a complex mix of ongoing assignments, it might take several weeks to finish your investigation and submit your finding.   Perhaps longer if you need to amend the allegation and wait for a new student response.

Since the deadline for submitting your finding is based on the grade entry deadline, you’ll have less time to do this step if you submit the initial allegation very late in the term.

Once you file your finding, the student has 5 business days to request an appeal hearing    If they do this, we are expected to hold the appeal hearing within 20 business days.   (Extensions are possible if there are compelling reasons for a delay.)

## Sanctions

If there are multiple infractions in the same FAIR allegation, use your best judgment about how to add up the penalties.   It’s important to consider the total amount of work involved.   E.g. plagiarizing a sequence of very small assignments could be regarded as similar to plagiarizing one bigger assignment.

There are two ways for a FAIR allegation to cause a student to fail the course:

* You directly select the “failing grade for the course” option in FAIR.
* You reduce/zero grades or deduct points, which pulls their course average down to where they fail.

The first option suggests that the offense was particularly severe, and any appeal will be heard by a college committee. The second option is generally preferable, and any appeal will be heard at the department level.

It’s much more serious if they commit a new infraction after you’ve filed one FAIR allegation.  This is rare and you should feel free to throw the book at them.

When students are working in groups, you must assess each student’s individual responsibility for the infraction.  The student code does not allow collective punishment.

Do not plea bargain, i.e. suggest a lighter sanction in exchange for a confession.   Students must be left with a free choice about whether to appeal.

## Plagiarism and facilitation

If two or more students submit very similar work, it is frequently not obvious whether one was the author, they worked together, or both copied from some external source (e.g. github, ChatGPT).   If the work was submitted using a system that collects a timestamped submission history, make sure to include this in your \`case file’ as well as your consideration, as it may provide additional perspective.  If no information is available that clarifies authorship, it is often best to file both as plagiarism allegations.

By the time you write your finding, student responses and additional information often give you a better picture of how the work was actually created.   So you may need to update the choice of infraction on FAIR.    This does not normally require sending the case back to the initial allegation stage.

* If one of them was the original author, update the author’s allegation to facilitation.
* If the students did the assignment together, update both allegations to cheating.

The student code definition of facilitation requires that it be deliberate or negligent.   So when one student was the author, you have a range of options to consider for the sanction.


* Deliberate facilitation often receives a sanction similar to plagiarism.
* The student code states that “Careless conduct that results in an infraction should be sanctioned less severely than intentional conduct.”   The details depend on exactly how negligent they were.
* If the author did little or nothing wrong and their work was stolen, drop the allegation.

Similarly, you have a range of options for the sanction when two students worked together on a solo assignment, depending on factors such as how clear the course policies were.

## The role of course staff

In larger classes, the first suspicion is often raised by a member of your course staff. Staff often help with collecting and organizing evidence. However, with the possible exception of a few very experienced senior TAs, they do not have the training or maturity to take the matter further. It is your responsibility to decide whether to file charges, speak with the students, determine the appropriate punishment, and so forth.
