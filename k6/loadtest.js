import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 5 },   // ramp-up to 5 users
    { duration: '1m', target: 10 },   // ramp-up to 10 users
    { duration: '30s', target: 0 },   // ramp-down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests below 500ms
  },
};

const BASE_URLS = {
  fastapi: 'http://localhost:8000',
  flask: 'http://localhost:5000',
  pipeline: 'http://localhost:8002', // adjust port if needed
};

export default function () {
  // FastAPI: GET analytics
  let res1 = http.get(`${BASE_URLS.fastapi}/analytics/summary`);
  check(res1, { 'fastapi summary 200': (r) => r.status === 200 });

  // Flask: ML predict
  let res2 = http.get(`${BASE_URLS.flask}/ml/predict?inputText=cat`);
  check(res2, { 'flask predict 200': (r) => r.status === 200 });

  // Pipeline: Run ETL
  let res3 = http.get(`${BASE_URLS.pipeline}/v14/run`);
  check(res3, { 'pipeline run 200': (r) => r.status === 200 });

  sleep(1); // pause between iterations
}
