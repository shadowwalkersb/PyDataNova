// Save the original fetch
const originalFetch = window.fetch;
const inspector = document.getElementById('inspector')

// Override fetch
window.fetch = async function (...args) {
  const [resource, config] = args;

  // Log request info
  const requestInfo = {
    url: resource,
    method: (config && config.method) || "GET",
    headers: (config && config.headers) || {},
    body: (config && config.body) || null,
  };

  inspector.textContent = JSON.stringify(requestInfo, null, 2);
};
