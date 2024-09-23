import React, { useEffect, useState } from 'react';
import api from '../services/api';

const VideoFeed = () => {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    const fetchVideos = async () => {
      const response = await api.get('/videos/');
      setVideos(response.data);
    };
    fetchVideos();
  }, []);

  return (
    <div>
      {videos.map(video => (
        <div key={video.id}>
          <h3>{video.title}</h3>
          <video src={video.url} controls />
          <p>Votes: {video.votes.length}</p>
        </div>
      ))}
    </div>
  );
};

export default VideoFeed;
