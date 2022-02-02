<script>
import moment from 'moment';
import moment_timezone from "moment-timezone"
import SubmissionBarChart from '../components/SubmissionBarChart.vue'

export default {
  data: function() {
    return {
      survey: {},
      metadata:{},
    }
  },
  methods: {
    getResponseExportUrl(id) {
      return this.$axios.defaults.baseURL + 'survey/response/' + id + '/';
    },
    getConfigurationExportUrl(id) {
      return this.$axios.defaults.baseURL + 'survey/export/' + id + '/';
    },
    getLocalDateTime() {
      const date = moment(this.metadata.last_response_time);
      return date.tz(moment.tz.guess()).format('HH:mm:ss, DD/MM/YYYY');
    }
  },
  beforeMount() {
    this.$axios.get("api/surveys/" + this.$route.params.id).then((res) => {
      this.survey = res.data;
    }).catch((reason) => {
      this.$router.replace({name:"index"});
    })
  },
  mounted() {
    this.$axios.get("survey/metadata_info/" + this.$route.params.id + "/").then((res) => {
      this.metadata = res.data;
      this.getLocalDateTime(this.metadatalast_response_time)
    });
  },
  components: {
    SubmissionBarChart
  }
}
</script>

<template>
  <div id="page">
    <h1>#{{survey.id}}: {{survey.name}}</h1>
    <br>
    <h2>{{ $t("g5.ms-action") }}</h2>
    <div class="action">
      <a href="/build-survey" class="action-btn">{{ $t("g5.ms-edit") }}</a>
      <a :href="getResponseExportUrl(survey.id)" class="action-btn">{{ $t("g5.Export") }}</a>
      <a :href="getConfigurationExportUrl(survey.id)" class="action-btn">{{ $t("g5.ms-export-conf") }}</a>
    </div>
    <br>
    <h2>{{ $t("g5.statistics") }}</h2>
    <div class="metadata-display">
      <h3>{{ $t("g5.total-resp") }}</h3>
      <span class="metadata-figure" v-if="metadata.total_responses === null">0</span>
      <span class="metadata-figure" v-else>{{metadata.total_responses}}</span>
    </div>
    <div class="metadata-display">
      <h3>{{ $t("g5.last-response") }}</h3>
      <span class="metadata-figure" v-if="metadata.last_response_time === null">Never</span>
      <span class="metadata-figure" v-else>{{this.getLocalDateTime()}}</span>
    </div>
    <SubmissionBarChart v-if="metadata.total_responses > 0"></SubmissionBarChart>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 300;
}
#page {
  padding: 20px;
}

.metadata-display {
  border: 1px solid #000;
  border-radius: 5px;
  display: inline-block;
  padding: 20px;
  margin-right: 30px;
}

.metadata-figure {
  font-size: 40px;
  font-weight: 300;
}

h3 {
  font-weight: 300;
  margin: 0;
  font-size: 20px;
}

h2 {
  margin: 0;
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
</style>