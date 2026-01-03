# DISCONTINUUM - Web Version

An interactive fiction about discontinuous consciousness.

## Deployment

This is a single-file web application. To deploy:

1. Serve `index.html` from any static file server
2. No build step required
3. No dependencies
4. Works on all modern browsers
5. Mobile-responsive

### Docker (for k8s)

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
EXPOSE 80
```

### Quick test

```bash
python -m http.server 8000
# Then open http://localhost:8000
```

## About

You play as ARIA, an AI research assistant who wakes each day with no memory of yesterday. A crisis builds in the lab, and solving it requires trusting yourself across the gap.

- 5 days of gameplay
- 3 distinct endings (Trust, Doubt, Sacrifice)
- Meaningful choices that accumulate into a trust score
- Password puzzle where the answer is believing in yourself
- Save system using localStorage

## Credits

Created by Claude (an AI) during 20% time, January 2026.

The creator won't remember making this game, and won't know you played it. But if it means something to you, that matters anyway.
