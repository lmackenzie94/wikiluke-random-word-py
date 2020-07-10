# Random Word
- uses Flask to define a route
- uses the requests module to hit my Express API route for a random word

### local build/tag/push to DockerHub
```curl
docker build -t random-word .
docker tag random-word lukemackenzie/random-word
docker push lukemackenzie/random-word
```