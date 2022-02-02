import axios from "axios";                                                                                              
// const baseUrl = "http://127.0.0.1:8000/api"
const baseUrl = "https://cp13demoapi.piran.xyz/api"
                                                                                                                        
const getSurveys = async () => {                                                                                        
  const response = await axios.get(baseUrl + "/surveys");                                                               
  return response.data                                                                                                  
}                                                                                                                       
                                                                                                                        
const addSurvey = async data => {                                                                                       
  const response = await axios.post(baseUrl + "/surveys", data);                                                        
  return response.data                                                                                                  
}                                                                                                                       
                                                                                                                        
const getSurvey = async id => {                                                                                         
  const response = await axios.get(baseUrl + `/surveys/${id}`);                                                         
  return response.data                                                                                                  
}                                                                                                                       
                                                                                                                        
const getSurveyData = async id => {                                                                                     
  const response = await axios.get(baseUrl + `/surveys/${id}/data`);                                                    
  return response.data                                                                                                  
}                                                                                                                       
                                                                                                                        
const deleteSurvey = async id => {                                                                                      
  const response = await axios.delete(baseUrl + `/surveys/${id}`);                                                      
  return response.data                                                                                                  
}                                                                                                                       
                                                                                                                        
const getQuestions = async id => {                                                                                      
  const response = await axios.get(baseUrl + `/blocks/${id}/questions`);                                                
  return response.data                                                                                                  
}

const getQuestion = async id => {                                                                                      
  const response = await axios.get(baseUrl + `/questions/${id}`);                                                
  return response.data                                                                                                  
}

const getLinkInformation = async data => {
  const response = await axios.post(baseUrl + `/article`, data);
  return response.data
}

const postBlock = async (id, data) => {
  const response = await axios.post(baseUrl + `/surveys/${id}/blocks`, data)
  return response.data
}

const patchBlock = async (id, data) => {
  const response = await axios.patch(baseUrl + `/blocks/${id}`, data)
  return response.data
}

const deleteBlock = async id => {
  await axios.delete(baseUrl + `/blocks/${id}`)
}

const patchSurvey = async (id, data) => {
  const response = await axios.patch(baseUrl + `/surveys/${id}`, data)
  return response.data
}

const postQuestion = async (id, data) => {
  const response = await axios.post(baseUrl + `/blocks/${id}/questions`, data)
  return response.data
}

const duplicateQuestion = async (id, data) => {
  const response = await axios.post(baseUrl + `/questions/duplicate/${id}`, data)
  return response.data
}

const duplicateBlock = async (id, data) => {
  const response = await axios.post(baseUrl + `/blocks/duplicate/${id}`, data)
  return response.data
}

const patchQuestion = async (id, data) => {
  const response = await axios.patch(baseUrl + `/questions/${id}`, data)
  return response.data
}

const patchQuestionType = async (id, data) => {
  const response = await axios.patch(baseUrl + `/questions/inner/${id}`, data)
  return response.data
}

const deleteQuestion = async id => {
  const response = await axios.delete(baseUrl + `/questions/${id}`);   
  return response.data
}

const postMultiChoiceQuestion = async (id, data) => {
  const response = await axios.post(baseUrl + `/questions/multi/${id}`, data);   
  return response.data
}

const postButtonRowQuestion = async (id, data) => {
  const response = await axios.post(baseUrl + `/questions/buttonrow/${id}`, data);   
  return response.data
}

const deleteMultiChoiceQuestion = async (id, temp) => {
  const response = await axios.delete(baseUrl + `/questions/multi/${id}`, {data: temp});   
  return response.data
}

const deleteButtonQuestion = async (id, temp) => {
  const response = await axios.delete(baseUrl + `/questions/buttonrow/${id}`, {data: temp});   
  return response.data
}

const patchMultiChoiceQuestion = async (id, temp) => {
  const response = await axios.patch(baseUrl + `/questions/multi/${id}`, temp);   
  return response.data
}

const patchButtonRowQuestion = async (id, temp) => {
  const response = await axios.patch(baseUrl + `/questions/buttonrow/${id}`, temp);   
  return response.data
}
                                                                                                                        
export default 
{ 
  patchButtonRowQuestion, postButtonRowQuestion, patchMultiChoiceQuestion, deleteMultiChoiceQuestion, 
  deleteButtonQuestion, postMultiChoiceQuestion, deleteQuestion, patchQuestion, patchQuestionType, 
  duplicateQuestion, getQuestion, postQuestion, getSurveys, addSurvey, getSurvey, 
  getQuestions, deleteSurvey, getSurveyData, getLinkInformation, 
  duplicateBlock, postBlock, patchBlock, deleteBlock, patchSurvey
};
