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

  logInspector("Fetch Request", requestInfo);

  try {
    const response = await originalFetch(...args);
    const cloned = response.clone();
    logInspector("Fetch Response", {
        url: response.url,
        status: response.status,
        statusText: response.statusText,
        headers: [...response.headers],
        body: await cloned.text()
    });
    return response;
  } catch (error) {
    const err = {
      message: error.message,
      stack: error.stack,
      ...error
    };
    logInspector("Fetch Error", err);
    return err;
  }
};

function logInspector(title, obj) {
  inspector.textContent = `\n=== ${title} ===\n`;
  inspector.textContent += JSON.stringify(obj, null, 2) + "\n";
  inspector.scrollTop = inspector.scrollHeight; // Auto-scroll to bottom
}
