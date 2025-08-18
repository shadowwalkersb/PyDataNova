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

    // Clone response to read JSON without consuming original
    const cloned = response.clone();
    let data;
    try {
      data = await cloned.json();
    } catch {
      data = await cloned.text();
    }

    logInspector("Intercepted Response", {
      status: response.status,
      statusText: response.statusText,
      body: data,
    });

    return response; // return original response to continue normal flow
  } catch (err) {
    logInspector("Fetch Error", { error: err.toString() });
    throw err;
  }
};

function logInspector(title, obj) {
  inspector.textContent += `\n=== ${title} ===\n`;
  inspector.textContent += JSON.stringify(obj, null, 2) + "\n";
  inspector.scrollTop = inspector.scrollHeight; // Auto-scroll to bottom
}
