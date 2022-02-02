
<template>
  <div class="main">
  <h1>{{ $t("g5.My Surveys") }}</h1>
    <a @click="createSurvey" class="action-btn">{{ $t("g5.ms-create") }}</a>
    <label for="file-btn" class="action-btn">Import Survey</label>
    <input type="file" id="file-btn" style="visibility:hidden;" v-on:change="handleFileUpload()" accept="application/json">
    <br><br>
    <table id="survey-table">
      <!-- Survey dashboard -->
      <tr>
        <th>#ID</th>
        <th>{{ $t("g5.ms-title") }}</th>
        <th>{{ $t("g5.Survey Language") }}</th>
        <th>{{ $t("g5.ms-length") }}</th>
        <th>{{ $t("g5.Survey Status") }}</th>
        <th>{{ $t("g5.ms-action") }}</th>
      </tr>
      <tr v-for="survey in surveys" :key="survey.id">
        <td>{{survey.id}}</td>
        <td>{{survey.name}}</td>
        <td>{{survey.language}}</td>
        <td>{{survey.timelimitMinutes}}</td>
        <td>
          <span v-if="survey.active === true"><i class="fas fa-circle" style="color:#18e200"></i> {{ $t("g5.Active") }}</span>
          <span v-else><i class="fas fa-circle" style="color:grey"></i> {{ $t("g5.Inactive") }}</span>
        </td>
        <td style="padding-right: 0">
          <a class="action-btn" @click="editSurvey(survey.id)">{{ $t("g5.ms-edit") }}</a>
          <a :href="getStatUrl(survey.id)" class="action-btn">{{ $t("g5.ms-view-stats") }}</a>
          <a :href="getResponseExportUrl(survey.id)" class="action-btn">{{ $t("g5.Export") }}</a>
          <a :href="getConfigurationExportUrl(survey.id)" class="action-btn">{{ $t("g5.ms-export-conf") }}</a>
          <a class="action-btn" @click="deleteSurvey(survey.id)">Delete</a>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import SurveyBuilder from './SurveyBuilder';
window.onclick = function(event) {
  var modal = document.getElementById('surveyModal');
  if (event.target == modal) {
    modal.style.display = 'none';
  }
}

import store from "../store/SurveyBuilder.js";
import SurveyServices from "../services/SurveyServices";
import pubsub from 'pubsub-js';


export default {
  name: 'mySurvey',
  store: store,
  components: {SurveyBuilder},
  data() {
    return {
      surveys: [],
    };
  },
  methods: {
    editSurvey(id) {
      this.$router.push(`build-survey/${id}`)
    },
    handleFileUpload(e) {
      const selectedFile = document.getElementById('file-btn').files[0];
      console.log(selectedFile)
      this.$axios
      .post("survey/import/", selectedFile, {
        headers: {
          "content-type": "application/json",
        }
      } ).then((res) => {
        alert("Survey has been imported!");
      })
      .catch((reason) => {
        alert("Cannot import survey! Please check format!");
      });
    },
    async createSurvey() {
      const response = await SurveyServices.addSurvey({ 
          name: "Survey Title",
          language: "English",
          consentText: "qwerty",
          timelimitMinutes: "60",
          active: "1"
      });

      this.$router.push(`build-survey/${response.id}`)

    },
    async deleteSurvey(id) {
      if (confirm(`Are you sure you want to delete survey with id ${id}?`)) {
        await SurveyServices.deleteSurvey(id)
        let index = this.surveys.indexOf(this.surveys.filter(e => e.id == id)[0])
        this.surveys.splice(index, 1)
      }

    },
    getSurveys() {
      this.$axios.get('api/surveys/', {}).then(res => {
            this.surveys = res.data;
          },
      );
    },
    getResponseExportUrl(id) {
      return this.$axios.defaults.baseURL + 'survey/response/' + id + '/';
    },
    getConfigurationExportUrl(id) {
      return this.$axios.defaults.baseURL + 'survey/export/' + id + '/';
    },
    getStatUrl(id) {
      return "/survey/" + id;
    }
  },
  beforeMount() {
    this.getSurveys();
  },
  mounted() {
    this.$axios.get('account/user/', {
      headers: {
        'Authorization': 'Token ' + localStorage.getItem('token'),
      },
    }).catch(reason => {
      //update user status
      pubsub.publish('logoutAction', false);
      //remove token when logout
      localStorage.removeItem('token');
      this.$router.replace({
        name: 'login',
      })
    });
  }
};
</script>

<style scoped>
.main {
  padding: 30px;
}

#survey-table {
  border-collapse: collapse;
}

#survey-table tr {
  border-bottom: 1px solid black;
}

#survey-table td {
  padding: 8px 30px 8px 0px;
  min-width: 100px;
  text-align: left;
}

#survey-table th {
  text-align: left;
  font-weight: 300;
}

.my-survey-wrapper {
  width: 100%;
  height: 800px;
  background-color: white;
  position: relative;
  display: flex;
  flex-wrap: wrap;
}

.my-survey-item {
  margin-left: 75px;
  margin-top: 50px;
  flex-basis: 25%;
  padding-left: 8px;
  padding-right: 8px;
  width: 200px;
  height: 250px;
  position: relative;
  border-style: solid;
  border-width: 5px;

}

.action-btn {
  border: 1px solid black;
  padding: 5px 10px;
  color: black;
  font-size: 15px;
  border-radius: 5px;
  text-decoration: none;
  margin: 2px 10px 2px 0px;
  display: inline-block;
}

.moreInfoB {
  position: absolute;
  left: 5px;
  bottom: 5px;
  border: 1px solid black;
  padding: 5px;
  color: black;
  background-color: white;
  border-radius: 10px;
  font-size: 15px;
}


.action-btn:hover {
  opacity: 0.5;
}

/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content */
.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.myChart {
  border: solid;
}

/* The Close Button */
.close {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
</style>