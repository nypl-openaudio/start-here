# Open Audio Weekend


Welcome to the repo for [Open Audio Weekend](http://togetherwelisten.nypl.org/openaudio/), hosted at The New York Public Library, June 25-26, 2016. This document contains materials and logistics for orienting participants to our 2 days of prototyping, creating, and sharing new approaches to audio accessibility for the public good.

# Projects  
The organizing team is grateful for the group of talented and engaged community members who brought together a diverse and impressive set of skills to make this weekend a success. To read more about the projects and prototypes conceived during the event, please visit our [Projects page](https://github.com/nypl-openaudio/start-here/blob/master/projects.md).

# Table of Contents  
1. [Logistics](#logistics)
2. [Schedule](#schedule)
3. [Open Audio Weekend Code of Conduct](#open-audio-weekend-code-of-conduct)
4. [Prompts](#prompts)
5. [Materials](#materials)
6. [Resources](#resources)
7. [Slack & Social Media](#slack--social-media)
8. [New to Git or Github?](#new-to-git-or-github)
9. [Sharing Your Project](#sharing-your-project)
10. [Documentation Policy](#documentation-policy)


## Logistics  
Open Audio Weekend is being held in the Celeste Bartos Forum of The New York Public Library's central branch, the [Stephen A. Schwarzman Building](http://www.nypl.org/locations/schwarzman). The Celeste Bartos Forum is on the ground floor of the library and is accessable through the Library entrance on 42nd Street. This entrance is wheelchair accessible. Upon entering at 42nd Street, the forum is directly opposite this entrance.   

At the start of both Saturday and Sunday, event volunteers will be stationed outside the entrance of the forum and available for questions. Throughout the event, staff and volunteers will be available to attendees.  

## Schedule

|  | Saturday, June 25th |
| :---: | --- |
| 10:00 AM |	Registration & coffee |
| 10:30 AM |	Introductions & agenda for the day |
| 11:30 AM |	Group working session |
| 1:00 PM |	Lunch provided |
| 2:00 PM |	Group working session |
| 5:00 PM |	Day 1 ends |

|  | Sunday, June 26th |
| :---: | --- |
| 10:00 AM |	Day 2 begins, coffee, group working session |
| 1:00 PM |	Lunch provided |
| 2:00 PM |	Final group working session, prepare for shareout |
| 4:00 PM |	Final shareout |
| 5:30 PM |	Open Audio Weekend ends |

This is a big topic with a lot to discuss and discover. If you're interested in continuing conversation, collaboration, and creation beyond the hosted hours, here are a few suggested spots close to the Library.

* **[Bryant Park](http://www.bryantpark.org/)**: The Library's backyard with free wifi to boot.
* **[Southwest Porch](http://www.bryantpark.org/things-to-do/southwest_porch.html)**: Located in Bryan Park this bar serves food and free wifi.
* **[Slattery’s Midtown Pub](http://www.yelp.com/biz/slatterys-midtown-pub-new-york):** a local bar serving food and wifi.

## Open Audio Weekend Code of Conduct

In order to foster a productive and welcoming environment for this hackathon, we request that all participants read the [NYPL Rules & Regulations](http://www.nypl.org/help/about-nypl/legal-notices/rules-and-regulations) document, which will serve as the code of conduct for the event.

## Prompts
As you know, Open Audio Weekend is a two-day hackathon to make audio accessible for the public good. It’s a big challenge to tackle so we’ve compiled some prompts to stimulate conversations and project ideas!  

* **Discover**: What new experiences can we make around discovery of audio?  
* **Find**: How can we make it easier to search audio?  
* **Listen**: What are some meaningful ways we can augment the experience of listening to audio?  
* **Share**: How can we make it easier to share audio?  
* **Learn**: What can we learn from audio? How can audio be used in an educational context?  
* **Engage**: How can we engage a community through audio?  
* **Access**:  How can we make audio collections more usable for people with disabilities?  

## Materials

Information regarding how to obtain audio and transcripts provided by the Open Audio Weekend partners can be found in [the Materials section](https://github.com/nypl-openaudio/start-here/tree/master/materials).

## Resources

### Speech Recognition, Speech To Text, Transcripts

* [CMUSphinx](http://cmusphinx.sourceforge.net/) - a group of open-source speech recognition systems developed at Carnegie Mellon University.
* [Kaldi](http://kaldi-asr.org/) - a toolkit for speech recognition written in C++ and licensed under the Apache License v2.0
* [p2fa-vislab](https://github.com/ucbvislab/p2fa-vislab) - A script for audio/transcript alignment written in Python.
* [Gentle](https://github.com/lowerquality/gentle) - Robust yet lenient forced-aligner built on Kaldi. A tool for aligning speech with text.
* [Open Transcript Editor](https://github.com/NYPL/transcript-editor) - an open-source, self-hosted, web-based tool for correcting transcripts that were automatically generated using speech-to-text software via auto-transcription services such as [Pop Up Archive](https://popuparchive.com/). It is being developed by [NYPL Labs](http://www.nypl.org/collections/labs) in partnership with [The Moth](http://themoth.org/) and [Pop Up Archive](https://popuparchive.com/) with generous support from the [Knight Foundation](http://www.knightfoundation.org/grants/201551666/). Example implementations can be found at:
  * [The NYPL Community Oral History Transcript Editor](http://transcribe.oralhistory.nypl.org/)
  * [StoryScribe by The Moth](http://storyscribe.themoth.org/)
  * [Open Audio Weekend](https://opentranscript.herokuapp.com/) - contains transcripts specifically for this event

### Audio Analysis

* [Praat](http://www.fon.hum.uva.nl/praat/) - a free scientific computer software package for the analysis of speech in phonetics
* [Sonic Visualiser](http://www.sonicvisualiser.org/) - a free application for viewing and analyzing the contents of audio files
* [WaveSurfer](http://www.speech.kth.se/wavesurfer/) - a free audio editor widely used for studies of acoustic phonetics

### Audio Manipulation, Converters

* [FFmpeg](http://ffmpeg.org/) - a free software project that produces libraries and programs for handling multimedia data
* [Audacity](https://sourceforge.net/projects/audacity/) - A free multi-track audio editor and recorder
* [VLC media player](http://www.videolan.org/vlc/index.html) - open source cross-platform multimedia player; useful for media file conversion (e.g. mp3 -> wav)
* [Pydub](http://pydub.com/) - Manipulate audio with python
* [Audio clipping tool](https://github.com/popuparchive/audiosearch-cookbook/wiki/Clipmaker). "Give us an audio file, an image, and some timestamped text and we'll give you a brief video that you can download or tweet." part of the [Audiosear.ch API](https://www.audiosear.ch/) cookbook.

### Audio Synthesis, Programming

* [Csound](http://csound.github.io/) - a computer programming language for sound
* [ChucK](http://chuck.cs.princeton.edu/) - a concurrent, strongly timed audio programming language for real-time synthesis, composition, and performance
* [Pure Data](http://puredata.info/) - a visual programming language for creating interactive computer music and multimedia works
* [SuperCollider](http://supercollider.github.io/) - an environment and programming language for real-time audio synthesis and algorithmic composition
* [FluidSynth](http://fluidsynth.sourceforge.net/) - a free open source software synthesizer
* [Timbre.js](http://mohayonao.github.io/timbre.js/) - a functional processing and synthesizing audio for the web
* [Flocking](http://flockingjs.org/) - a JavaScript audio synthesis framework designed for artists and musicians

### Data

* [Audiosear.ch API](https://www.audiosear.ch/) - Full text search & recommendation API for podcasts and radio. [Free API](https://audiosear.ch/developer) is also available.

### Accessibility

* [WebAIM: Web Accessibility in Mind](http://webaim.org/resources/) -
Website with a number of excellent resources and services around web accessibility many of which are highlighted in the [Resources Page](http://webaim.org/resources/).

## Slack & Social Media
We’ve set up an instance of Slack for use during the event. For those of you not familiar with Slack, it’s a chatroom allowing group and 1-on-1 conversations. To use the event Slack, just log in at: [togetherwelisten.nypl.org/openaudio/talk](http://togetherwelisten.nypl.org/openaudio/talk/).

The hashtag for our event is **#openaudio**. Please use it to tag your tweets, Instagrams & other posts related to the event!

## New to Git or Github?

[Git](https://git-scm.com/) is a file control system that lets people share and contribute to projects (called “repositories”), most of them software projects (but some people use it for other things, like [taco recipes](https://github.com/sinker/tacofancy)). Github (the website you are on now) is a company that allows anyone to host public Git projects for free.

We will use Git and Github to share the projects made during the Open Audio Weekend. If you're not a programmer, don't worry, sharing files in Github is as easy as dragging and dropping files to your browser! For a quick introduction on creating and updating a repository on Github, read the [Creating a Repository](https://help.github.com/articles/create-a-repo/) **(make sure the repository you create is Public)**, [Adding a File to a Repository](https://help.github.com/articles/adding-a-file-to-a-repository/), and [Editing Files in your Repository](https://help.github.com/articles/editing-files-in-your-repository/) tutorials. There are more examples in the [Github help](https://help.github.com/). There is also this [great introductory tutorial](http://ablwr.github.io/blog/2014/11/03/non-technical-persons-guide-to-becoming-an-open-source-software-contributor-via-github/) on how to become an open-source software contributor via Github by [Ashley Blewer](//github.com/ablwr).

Event volunteers will be on hand during the event to help out.

> **IMPORTANT:** All code you submit in the Open Audio Weekend should go to repositories you create in the [OpenAudio Organization](//github.com/nypl-openaudio). Make sure your repositories are public.

### Sharing Your Project

Every team will present their project at the end of Day 2. As [described above](#new-to-git-or-github), every project will have its own repository.

- **Make sure your project includes a README**: select “Initialize this repository with a README” when creating the repository and then [edit the file](https://help.github.com/articles/editing-files-in-your-repository) or just [add a `README.md` file later](https://help.github.com/articles/adding-a-file-to-a-repository) (it is just a regular text file with the `.md` file extension instead of `.txt`).
- Add this information to your README: project name, team members, project description, and links to all external assets (those outside of the repository). Make sure to take advantage of [Github's text formatting toolbar](https://help.github.com/articles/about-writing-and-formatting-on-github/).
- If your project is an app (web or otherwise), **make sure to include screenshots.**
- Depending on your type of project you may [add additional files](https://help.github.com/articles/adding-a-file-to-a-repository/) so you can present and share your project. Ask any of the volunteers if you have any questions on how to use Github.

During the final shareout you will use this repository and README as launchpad for your presentation. All projects will be presented from the same computer which will be connected to the projector so make sure to have all the necessary links in there!

## Documentation Policy  

Participants of this event may be photographed or filmed for educational and promotional purposes. Please notify staff if you do not wish to be photographed or filmed.

[Return to Top](#open-audio-weekend)
