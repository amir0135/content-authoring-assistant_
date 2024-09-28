// test.js
// This script is for load testing using K6.
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 10 },  // Ramp up to 10 users over 30 seconds.
    { duration: '1m', target: 10 },   // Hold at 10 users for 1 minute.
    { duration: '30s', target: 0 },   // Ramp down to 0 users over 30 seconds.
  ],
};

export default function () {
  let res = http.post('http://localhost:8000/generate-text/', JSON.stringify({
    "prompt": "Write me a blog post",  // Sample payload for generating text.
    "max_tokens": 256,
    "temperature": 0.7
  }), { headers: { 'Content-Type': 'application/json' } });

  check(res, {
    'status was 200': (r) => r.status == 200,  // Check if status is 200 OK.
    'response time was < 10s': (r) => r.timings.duration < 10000,  // Ensure response time is under 10 seconds.
  });

  sleep(1);  // Pause between requests.
}