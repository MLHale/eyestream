---
title: 'Eyestream: An open WebSocket-based middleware for serializing and streaming eye tracker event data from Gazepoint GP3 HD research hardware'
tags:
  - Python
  - eye tracker
  - Gazepoint 
  - websocket
  - JSON
  - streaming
authors:
  - name: Matthew L. Hale
    orcid: 0000-0002-8433-2744
    affiliation: 1
affiliations:
 - name: School of Interdisciplinary Informatics, University of Nebraska at Omaha
   index: 1
date: 21 April 2019
bibliography: paper.bib
---

# Summary
Eye trackers enable a wide range of research and development activities in academia, medicine, and industry. Researchers and developers using eye trackers are able to collect rich user interaction data such as user fixation durations, points of gaze, and 3D models of user pupils that enable unique analysis and applications in areas such as user-interaction design, rehabilitative/restorative medicine, and marketing. Most eye trackers, including the two with the largest market share `Gazepoint GP3 HD`[@gazepoint] and the `Tobii Pro X3-120` [@olsen2012tobii], ship with proprietary desktop software packages that collect, house, and analyze captured data. This closed source delivery model makes it difficult for researchers and developers to directly interact with raw eye tracker data, which prevents custom analysis and hinders application development and integration efforts. Further, most closed-source eye tracker analysis tools do not support streaming and real-time analysis applications.

While the Gazepoint GP3 HD[@gazepoint] is designed to work with Gazepoint’s proprietary analysis software, it also provides an underutilized alternative low-level XML-based API called OpenGaze for extracting data from the hardware. We have created a tool on top of OpenGaze called `Eyestream`. `Eyestream` is capable of serializing hardware-captured eye tracker data as JSON and streaming it in real-time, at frequencies up to 150hz, to desktop, web, or mobile applications. `Eyestream` is an open source package designed to operate as middleware between the Gazepoint GP3 and applications that consume eye tracker data for analysis or visualization purposes. It was implemented using Python 2.7, a web socket server framework called `Django Channels`[@djangochannels], an in-memory database caching tool called `Redis`[@carlson2013redis], and a modified version of `PyOpenGaze`[@esdalmaijer2017]. `Eyestream` is containerized using `Docker` [@boettiger2015docker]. 

![Figure 1: System-level Architecture of Eyestream](assets/paper-040a5e2f.png)
> Figure 1: System-level Architecture of Eyestream
 
# Eyestream and Its Uses
`Eyestream` provides a real-time streaming interface to other software applications that enable a wide-variety of applications. The streaming interface is built using websockets. Any application on any platform or written in any language can interact with `Eyestream` provided that it can establish a websocket. All major languages (C/C++/C#, Python, Java, JavaScript, Ruby, Go, etc) have direct or library support for websockets, making `Eyestream`'s approach widely open. Figures 2, 3, and 4 show the `Eyestream` platform from three perspectives: 2) The `Eyestream` server running in the command line, 3) Eyestream's invocation of the underlying Gazepoint eye monitoring software, and 4) a console, in Google Chrome Developer Tools, printing streaming eye data it is receiving from the server.

	
![Figure 2: Eyestream's websocket server running on console](assets/paper-9af5c794.png)
> Figure 2: Eyestream's websocket server running on console

![Figure 3: Gazepoint's real-time eye monitor invoked by Eyestream](assets/paper-b1451bff.png)
> Figure 3: Gazepoint real-time eye monitor invoked by Eyestream

![Figure 4: Data streaming to a browser is printed in the console](assets/paper-aa2d526c.png)
> Figure 4: Data streaming to a browser is printed in the console


One common use for real-time eyetracker data is the generation of real-time heatmaps showing the temporal progression of user eye movements. An example application using `Eyestream` to build real-time heatmaps is shown in Figure 5. This application, called `Cybertrust`, is a research and training platform that helps users identify phishing attempts. In this example, as the user’s gaze travels across the screen (depicted as the black line), the heatmap overlay gradually changes color to reflect the amount of time spent fixating on a particular area. Heatmap data is rendered using a D3 plot so that users and trainers can see what they are focusing on within phishing content. 

Other possible applications for `Eyestream` include medical tools for restorative eye or stroke care [@kasten2006visual], examining areas of interest within a page for UI design or marketing [@goldberg2002eye], and as an interaction modality for video games [@corcoran2012real] or virtual reality systems.

![Figure 5: Heatmap of Eye Movements as viewed in a phishing training app](assets/paper-d53b90c0.png)
> Figure 5: Heatmap of Eye Movements as viewed in a phishing training app
 
# On-going research projects using Eyestream
Eyestream is currently in use within the `Cybertrust` phishing research platform [@hale2015cyberphishing] [@hale2015measuring] [@hale2016apriori] [@hefley2018multimodal]. `Cybertrust` is a gamified experimentation platform used to identify factors related to phishing victimization. 

# License 
Eyestream is licensed under the GNU General Public License and can be found on the following GitHub repository: https://github.com/MLHale/eyestream.

# Acknowledgements

We acknowledge contributions by Gabi Wethor ([gewethor on GitHub](https://github.com/gewethor)) for her work in testing the installation and usage instructions.

# References
