<template>
  <div class="post">
    <img v-if="isImage" :src="question.articleImage" :alt="question.articleTitle" width="100%" height="auto" />
    <div v-else class="no-image">{{ $t("postEditable.noImage") }}</div>
    <p contenteditable @focusout="updateSource">
      {{ question.articleSource.toUpperCase() }}
    </p>
    <h1 contenteditable @focusout="updateTitle">{{ question.articleTitle }}</h1>
  </div>
</template>


<script>
import SurveyServices from "../../services/SurveyServices";
import store from "../../store/SurveyBuilder.js";

export default {
  name: "PostFacebook",
  store: store,
  props: {
    question: Object,
  },
  methods: {
    /**
     * Update and save source being changed
     */
    async updateSource(e) {
      store.commit("updateValue", {
        value: e.target.innerHTML,
        parent: this.question,
        key: "articleSource",
      });

      await SurveyServices.patchQuestionType(this.question.id, {
        articleSource: e.target.innerHTML,
      })
    },
    /**
     * Update and save title being changed
     */
    async updateTitle(e) {
      store.commit("updateValue", {
        value: e.target.innerHTML,
        parent: this.question,
        key: "articleTitle",
      });

      await SurveyServices.patchQuestionType(this.question.id, {
        articleTitle: e.target.innerHTML,
      })
    },
  },
  computed: {
    /**
     * Check whether it is an image or not
     * @returns {boolean} false if not an image and true otherwise
    */
    isImage() {
      if (
        this.question.articleImage === "" ||
        this.question.articleImage == null
      ) {
        return false;
      }

      return true;
    },
  },
};
</script>

<style scoped>
html:lang(ur) * {
  text-align: center;
}

.post {
  width: 600px;
  background-color: #f0f2f5;
  border-bottom: 1px solid #ced0d4;
  margin: 0 auto;
  margin-top: 30px;
  padding-bottom: 10px;
}

.no-image {
  background-color: #d1d9dd;
  height: 100px;
  width: 100%;
  color: black;
  text-align: center;
}

p {
  font-family: Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  font-size: 13px;
  line-height: 15px;
  text-align: left;
  color: #65676b;
  margin: 6px 16px;
}

h1 {
  font-family: Arial;
  font-style: normal;
  font-weight: bold;
  font-size: 17px;
  line-height: 20px;
  text-align: left;
  margin: 0 16px;
  color: #050505;
}
</style>
