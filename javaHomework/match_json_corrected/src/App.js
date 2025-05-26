import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [users, setUsers] = useState([]);
  const [posts, setPosts] = useState([]);
  const [selectedUserId, setSelectedUserId] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [usersResponse, postsResponse] = await Promise.all([
          fetch('users.json').then(res => res.json()),
          fetch('posts.json').then(res => res.json())
        ]);
        setUsers(usersResponse);
        setPosts(postsResponse);
      } catch (error) {
        console.error('Ошибка загрузки данных:', error);
      }
    };

    fetchData();
  }, []);

  const selectedUser = users.find(user => user.id === selectedUserId);
  const userPosts = posts.filter(post => post.userId === selectedUserId);

  return (
    <div className="App">
      <div className="container">
        <div className="user-list">
          {users.map(user => (
            <div 
              key={user.id} 
              className="user-item" 
              onClick={() => setSelectedUserId(user.id)}
            >
              {user.name}
            </div>
          ))}
        </div>
        <div className="post-list">
          {!selectedUserId ? (
            <p><strong>Выберите пользователя</strong></p>
          ) : (
            <>
              {selectedUser && (
                <div className="user-info">
                  <h2>{selectedUser.name}</h2>
                  <p>Username: <strong>{selectedUser.username}</strong></p>
                  <p>Email: <strong>{selectedUser.email}</strong></p>
                  <p>Phone: <strong>{selectedUser.phone}</strong></p>
                  <p>Website: <strong>{selectedUser.website}</strong></p>
                  <p>Address: <strong>
                    {selectedUser.address.street}, {selectedUser.address.suite}, 
                    {selectedUser.address.city}, {selectedUser.address.zipcode}
                  </strong></p>
                  <p>Company: <strong>{selectedUser.company.name}</strong></p>
                </div>
              )}
              {userPosts.map(post => (
                <div key={post.id} className="post-item">
                  <h3>{post.title}</h3>
                  <p>{post.body}</p>
                </div>
              ))}
            </>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;