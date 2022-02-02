<template>
  <div class="options">
    <h1 class="close-header">{{ $t('pOptionsArticles.socialPostFormat') }}</h1>
    <dropdown-base
      :options="['Twitter', 'Facebook']"
      :icons="['fab fa-twitter', 'fab fa-facebook']"
      :currentType="question.articleStyle"
      @input="handlePostStyle"
      class="secondary-drop"
    />
    <line-base class="dark" />

    <h1>{{ $t('pOptionsArticles.socialEngagement') }}</h1>
    <line-base class="light" />

    <div class="text-with-button">
      <h2>{{ $t('pOptionsArticles.likeCount') }}</h2>
      <toggle-base
        :toggled="question.articleLikesOn"
        @handleToggle="activateLikeCount"
      ></toggle-base>
    </div>
    <div class="text-with-button">
      <h2>{{ $t('pOptionsArticles.commentCount') }}</h2>
      <toggle-base
        :toggled="question.articleCommentsOn"
        @handleToggle="activateCommentCount"
      ></toggle-base>
    </div>
    <div class="text-with-button">
      <h2>{{ $t('pOptionsArticles.shareCount') }}</h2>
      <toggle-base
        :toggled="question.articleSharesOn"
        @handleToggle="activateShareCount"
      ></toggle-base>
    </div>

    <line-base class="dark" />
  </div>
</template>

<script>
import SurveyServices from "../../services/SurveyServices";

import DropdownBase from "./DropdownBase.vue";
import LineBase from "./LineBase.vue";
import ToggleBase from "./ToggleBase.vue";
import store from "../../store/SurveyBuilder.js";

export default {
  name: "PanelOptionsArticle",
  store: store,
  components: {
    ToggleBase,
    LineBase,
    DropdownBase,
  },
  props: {
    question: Object,
  },
  methods: {
    /**
     * Change and save the post style of a news post question
     */
    async handlePostStyle(style) {
      store.commit("updateValue", {
        parent: this.question,
        key: "articleStyle",
        value: style,
      })

      await SurveyServices.patchQuestionType(this.question.id, {articleStyle: style})
    },
    /**
     * Toggle and save whether to have like count or not
     */
    async activateLikeCount() {
      store.commit('toggle', { parent: this.question, key: 'articleLikesOn' })

      await SurveyServices.patchQuestionType(this.question.id, {articleLikesOn: this.question.articleLikesOn})
    },
    /**
     * Toggle and save whether to have comment count or not
     */
    async activateCommentCount() {
      store.commit('toggle', { parent: this.question, key: 'articleCommentsOn' })

      await SurveyServices.patchQuestionType(this.question.id, {articleCommentsOn: this.question.articleCommentsOn})
    },
    /**
     * Toggle and save whether to have share count or not
     */
    async activateShareCount() {
      store.commit('toggle', { parent: this.question, key: 'articleSharesOn' })

      await SurveyServices.patchQuestionType(this.question.id, {articleSharesOn: this.question.articleSharesOn})
    }
  },
};
</script>

<style scoped>
html:lang(ur) * {
  text-align: right;
}

h1,
h2 {
  color: black;
  padding: 0 16px;
  font-family: Arial, Helvetica, sans-serif;
  font-style: normal;
  text-align: left;
}

h1 {
  font-size: 16px;
  font-weight: bold;
  padding: 16px;
}

h2 {
  font-size: 16px;
  font-weight: bold;
}

.close-header {
  padding-bottom: 0px;
}

.text-with-button {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  align-content: center;
}

.secondary-drop {
  z-index: 9;
}
</style>