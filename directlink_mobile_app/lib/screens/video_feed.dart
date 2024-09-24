import 'package:flutter/material.dart';
import '../services/api_service.dart';

class VideoFeed extends StatefulWidget {
  @override
  _VideoFeedState createState() => _VideoFeedState();
}

class _VideoFeedState extends State<VideoFeed> {
  final ApiService apiService = ApiService();
  List<dynamic> videos = [];

  @override
  void initState() {
    super.initState();
    loadVideos();
  }

  Future<void> loadVideos() async {
    try {
      final fetchedVideos = await apiService.fetchVideos();
      setState(() {
        videos = fetchedVideos;
      });
    } catch (e) {
      // Handle error
      print(e);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('DirectLink'),
        ),
        body: ListView.builder(
          itemCount: videos.length,
          itemBuilder: (context, index) {
            final video = videos[index];
            return Card(
              child: Column(
                children: [
                  Text(video['title']),
                  // Placeholder for video player
                  Container(
                    height: 200,
                    color: Colors.black12,
                    child: Center(child: Text('Video Player Placeholder')),
                  ),
                  Text('Votes: ${video['votes'].length}'),
                ],
              ),
            );
          },
        ));
  }
}
