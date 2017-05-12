# Attendance-Tracking

## Phases Overview

1. Capture pictures (crawler/mining ?)

2. Use opencv to generate 'targetFace rectangle' on identified faces (instead of using Detect Face API)

3. Manually label faces

4. Integrate with Azure Face API: 

  - Create Person Group
  
  	- Reference: [Doc](https://southeastasia.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395244)
  
  - Create Person
  
  	- Reference: [Doc](https://southeastasia.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523c)
  
  - Add Faces to Person (no more than 248 faces / person)
  
  	- Reference: [Doc](https://southeastasia.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523b)

5. Train Person Group

6. Test with testing data (more pictures needed)

7. Build an Authentication system using camera and Identify/Verify Face API (may have to use Detect Face API)

## Useful links:

- [How to Identify Faces in Image - Microsoft](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/howtoidentifyfacesinimage)

- [Tutorial code for Python27 + OpenCV3 Facial Recognigtion - Github](https://github.com/shantnu/Webcam-Face-Detect)

- [Face API Swagger](https://southeastasia.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/export?DocumentFormat=Swagger&ApiName=Face%20API%20-%20V1.0) (use to import to postman for testing)

