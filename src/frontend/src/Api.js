// src/Api.js
const apiUrl = process.env.REACT_APP_API_URL;

export const createUser = async (name, email) => {
  const response = await fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name, email }),
  });
  if (!response.ok) {
    const errorMessage = `Failed to create user: ${response.statusText}`;
    throw new Error(errorMessage);
  }
  return await response.json();
};

export const getUsers = async () => {
  const response = await fetch(apiUrl);
  if (!response.ok) {
    const errorMessage = `Failed to fetch users: ${response.statusText}`;
    throw new Error(errorMessage);
  }
  return await response.json();
};

export const getUserById = async (userId) => {
  const response = await fetch(`${apiUrl}/${userId}`);
  if (!response.ok) {
    const errorMessage = `Failed to fetch user ${userId}: ${response.statusText}`;
    throw new Error(errorMessage);
  }
  return await response.json();
};
