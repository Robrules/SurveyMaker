<template>
  <div class="post">
    <img v-if="isImage" :src="question.articleImage" :alt="question.articleTitle" width="100%" height="auto" />
    <div v-else class="no-image">{{ $t("postEditable.noImage") }}</div>
    <h1 contenteditable @focusout="updateTitle">{{ question.articleTitle }}</h1>
    <h2 contenteditable @focusout="updateSnippet">
      {{ question.articleSnippet }}
    </h2>

    <p contenteditable @focusout="updateSource">{{ question.articleSource }}</p>
  </div>
</template>


<script>
import SurveyServices from "../../services/SurveyServices";
import store from "../../store/SurveyBuilder.js";

export default {
  name: "PostTwitterEditable",
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
    /**
     * Update and save snippet being saved
     */
    async updateSnippet(e) {
      store.commit("updateValue", {
        value: e.target.innerHTML,
        parent: this.question,
        key: "articleSnippet",
      });

      await SurveyServices.patchQuestionType(this.question.id, {
        articleSnippet: e.target.innerHTML,
      })
    },
  },
  computed: {
    /**
     * Check whether it is an image or not
     * @returns {boolean} false if not an image and true if it is
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
  width: 420px;
  background-color: white;
  border: 1px solid #d1d9dd;
  margin: 0 auto;
  padding-bottom: 10px;
  border-radius: 14px;
  overflow: hidden;
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
  font-size: 14px;
  line-height: 15px;
  text-align: left;

  color: #65676b;
  margin: 6px 12px 0px;
}

h1,
h2 {
  font-family: "Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI",
    Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 16px;
  text-align: left;

  margin: 6px 12px 2px;
}

h1 {
  color: #101419;
  margin: 6px 12px 2px;
}

h2 {
  color: #566370;
  font-weight: 500;
  margin: 4px 12px 2px;
}
</style>
