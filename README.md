### Trustlab Assessment

#### Subproblem Solved
The repository consists of an implementation of an API which could be used by social platform developers to analyze the comments before they are posted on their platform and also make decisions on the user feedback recieved for various posted comments.
- Analyzing comments to be posted: Using the embeddable HTML provided for an input element the user of the platform would recieve real-time feedback on their comments and suggestions to improve based on the feedback. As the user will type their comment a request would be sent to the API endpoint `analyze` when they are "done-typing".
- Analyzing user feedback for comments: Another part of the embeddable HTML is a two-button system for reporting a comment on the platform. The API then responds with what it believes the comment's "hate speech score" is, then the developer can decided how to handle this particular case.

#### API Usage (from a platform developer's perspective)
The platform developer can use the HTML `embed` tag to get the benefits of the data-store in place through the API. Based on their design decisions the developer can either display the feedback string received as real-time feedback for the user or also use it to analyze the comment before adding it to their platform.  
The developer can also use a combination of the user feedback received for a comment and the API's feeback (`val` key in the JSON response) to make a decision over the action to be taken against a comment.  
The developer can also use the `/analyze` endpoint directly to get the "hate speech" score of any text block in question and thus the API provides a great deal of flexibility

##### Endpoints
- `/` : This endpoint returns the `embed` HTML, thus servses as home page for testing the API.
- `/<int>` : This a test endpoint. The integer value sent through the request sets the percentage value that the hypothetical model would return as the "hate speech score" for a comment. This can be used to test the various scenarios that might arise when deploying the API in the real world.
- `/embed` : This returns the HTML that can be embedded. This endpoint would be used by a platform developer while requesting for the embeddable HTML through the `embed` tag.
- `/analyze` : This endpoint recieves the text submitted and calls the hypothetical model in place for a "hate speech score" for the particular string. And then returns JSON object of the form,

```python
{
    "feeback": A string consisting of the percentage score and a suggestion to edit if neccessary for the user,
    "value": An integer value for the percentage score. This could be used by a developer to make a decision 
             over the action to be taken for a particular comment.
}
```

#### Assumptions
- Only solving the subproblem for detecting and taking action against hate speech.
- I assumed that there is already a model in place which is trained to detect and provide a "hate speech score" for a string in percentage as JSON object.

#### Running the API locally
Run the following command in the api directory,
```
python3 api.py
```
Then go to the address `127.0.0.1:5000` in the browser which should serve a page with a text area where a comment can be typed and the real time feedback would be displayed underneath. The page also consists of an example comment and two buttons `+` `-` to report if a comment is "good" or "bad". Clicking these buttons sends a request to the API and response received is displayed. However a developer can use the response obtained according to their design decisions i.e. one scenario could be to add the response to the comments database and remove the comment whenever its score reaches a certain threshold.  
For testing purposes the `/<int>` endpoint can be used. By default it is assumed that the model responds with a `56%` hate speech score for the comment, sending a request to say `/86` would reload the page and change the value to `86%` thus different scenarios can be tested.  
> Since this a constant value in the backend we can test this by monitoring the `Network` tab thus ensuring that the results html text is actually updated in real time as the user types.

#### Dependencies
Python Packages: 
- Flask
- json

#### Possible Improvements
- We could significantly improve the aesthetics of the embedded components so that they can be used directly by a developer without style modifications.
- Currently, for a proof a concept, both the "features", real time feeback & user feedback are in the same embeddable component they can be separated for to expand the use cases for the API.
- We can implement a user login (through API keys) and provide the developers with a way to obtain plots like scatter plots of word frequencies etc. for the comments posted on their platform. This could be used to make major user policy related decisions for the platform.

