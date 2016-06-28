# InstaBurns  
#### Short Description  
Process audio transcripts, apply common topics, gather visual resources, and build illustrative slideshows. Use the topics and images for discovery and navigation.  

#### Theme  
Discovery  

#### Links and Materials  
[Demo Presentation](https://github.com/nypl-openaudio/start-here/blob/master/Projects/Images/%E2%80%9CInstaBurns%E2%80%9D%20Visual%20Navigator.pdf)

#### Long Description  
Our goal was to help users explore large collections of audio and discover thematic relationships. The challenge is “seeing” an overview of what is inside a specific audio file, diving in more deeply, and using that as a launch-point for serendipity and discovery.  

We considered three primary audiences and a range of user scenarios  

**Public users**  
* Casual, undirected exploring and sharing  
* Discovering “in place” -- using audio to enrich an experience in a neighborhood, monument, or landmark  

**Researchers and students who want to gather resources related to topics of interest**  
* Collecting segments of audio and organizing references as part of larger research projects  
* Archivists and resource managers  
* Answering questions from others about finding or using specific audio resources  
* Performing background research when creating new works  

#### Our process
**The design process involved**  
Elaborating the scenarios to understand the nuances of the user’s experience  
Mapping out general flows for the scenarios, to understand the interactions required for the overall experience.   
Parallel design activities rapidly produced wireframes and consensus around the behavior of the main features.   
We focused on the audio player screen for development, but thought through concepts for other supporting screens.  

**Development had four threads**  
* Perform cluster analysis on the transcripts to identify common terms and co-occurrence relationships that could suggest themes, and implement a visualization to explore the relationships between terms across different audio files.   
* Name the emerging themes to create high-level categorization of segments within each audio file.  
* In parallel, perform a semantic analysis of the sentences in the transcript; using the resulting significant terms, use the Google image API to retrieve images associated with the key phrases in each sentence, and stream them real-time into a viewer to create a background slideshow that provides a visual reference aligned with the audio narrative.  
* Create an application that presents the streaming images, transcript, and the waveform with topics mapped to segments of the audio; also show additional reference links to other audio files and external resources/sites.  




#### 
