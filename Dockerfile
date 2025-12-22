2025/12/22 20:44:54 report build steps to Koyeb API: HTTP client error: Post "https://app.koyeb.com/v1/provisioning/f593c3aa-264e-4f76-8b8e-3389feeefea9/status/build/1": context deadline exceeded
Build ready to start ▶️
2025/12/22 20:44:55 report step `git-clone` progress to Koyeb API: API returned status code 400
>> Cloning github.com/Fox455664/Fox66.git commit sha be7bc99dd8cd59cd2478003e24896740549e06de into /builder/workspace
Initialized empty Git repository in /builder/workspace/.git/
From https://github.com/Fox455664/Fox66
 * branch            be7bc99dd8cd59cd2478003e24896740549e06de -> FETCH_HEAD
HEAD is now at be7bc99 Create Dockerfile
2025/12/22 20:44:56 report step `git-clone` progress to Koyeb API: API returned status code 400
2025/12/22 20:44:56 report step `start-docker` progress to Koyeb API: API returned status code 400
Starting Docker daemon...
Waiting for the Docker daemon to start...
done
2025/12/22 20:44:58 report step `start-docker` progress to Koyeb API: API returned status code 400
2025/12/22 20:44:58 report step `build` progress to Koyeb API: API returned status code 400
2025/12/22 20:44:59 report step `build` progress to Koyeb API: API returned status code 400
Build failed ❌
#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 359B done
#1 DONE 0.0s
Dockerfile:1
--------------------
   1 | >>> cat <<EOF > Dockerfile
   2 |     FROM python:3.9-slim-buster
   3 |     
--------------------
error: failed to solve: dockerfile parse error on line 1: unknown instruction: cat (did you mean cmd?)
