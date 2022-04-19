## Getting Started

Following the requirement I made a script that can be executed using this command once you’ve clone the repository:

```bash
bash server/deployment/ci.sh
```

This will run 4 differents steps:

**Step 0: Basic requirement install**

I’ve assume that you already have `terraform` `helm` `kubectl` and `docker` installed but you may not have the package I’m using to format and lint the python server. So this step will install them but feel free to disregard it by using 

```bash
bash server/deployment/ci.sh --no-step-0
```

**Step 1: Lint and formatting**

As you would have it in a classic step CI the first thing you do is making sure your code follow your organisation standard regarding formatting and linting.
Here I’ve only use the commons packages as a POC but many other could be used

**Step 2: Running Test**

There is different school of thought here, some would prefer to build the docker image directly and then run it with a  special entrypoint making sure test are run in the same condition as the production image will run, other execute their source code in a dedicated environment matching their requirement and thus avoiding putting unecessary packages in the images. Best of both world being using multistage build when you can.
Here I’m only running the command I would have put in a CI job.

**Step 3: Building the docker image**

What’s intersting here is the tag used, (expect the minkube trick needed as I don’t have a registry). I’v decided to go with the current commit sha so I can see directly what code is running with that image. In a production environment git tag using a semver release system would be more adequate depending on the best practices of the organisation.

**Step 4: Deploying**

Deploy should be done in staging first or any QA environment that is setup. Also as I’ve mention in the CI script we should have publish the helm chart before deploying. Ensuring that the context for this specific release is always store in the chart release.
Since I’m using Helm, the terraform part I quite simple, and It rely on current kubectl context. In a production pipeline we would have to make sure that this context is made avaialble in the runner using ansible for instances.
I’m not a big fan of using terraform to deploy helm release as it mean adding yet another layer of HCL upon the verbosity of a YAML chart, but since it was a requirement.
As of why I’m using Helm ? This is becoming standard and now that features like reusable templates are available in helm 3 it has become IMO and indispensable assert for complex stack deployment.

## Limitation

I’ve lost some hair doing this project, the ugly truth of owning a Mac I guess.... Since docker is not directly running on my computer but through an embedded hypervisor accessing port with the command `minkube tunnel` is done via an ssh tunnel that unfortunately does not support udp forwarding (https://github.com/kubernetes/minikube/issues/12362) 

I didn’t had the time to test it on linux, but if we are in a production environment such access would be handle by a layer 3 loadbalancer using the current cloud provider of the organisation.

### Improvement

I’ve made some remark in the getting started but obviously there is a lot more that can be done:

- Better probe for liveness and readyness those are just dummy, we need to send a message to the udp port that perform some kind of check and respond with a status
- Request and Limit, those are not set making our node subject to intensive load, if one server was performing badly the scheduler need to take it down depending on our availability policy
- log & monitoring, logs are exported to the standard output we need an agent to send them to loki, datadog which ever dashboard we use. Same goes for metrics, those metrics will help us set correctly the request and limit and identifying bottlenecks.
- Autoscaling, once we have good request and limits putting in place an HPA and making sure there is room for the node pool to growth following our budget limit.
