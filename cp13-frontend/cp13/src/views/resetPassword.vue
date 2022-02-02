<template>
    <div class = "main">
      <meta name="viewport" content="width-device-width, initial-scale=1.0">
        <div class = "window">
          <!-- Reset password block -->
            <p class = "title">{{ $t("g5.Reset your password") }}</p>
            <img alt="" class="line" src="imagesine.png" />
            <p class = "msg">{{ $t("g5.Enter new password") }}</p>
            <input class = "input-box" type="text" v-model="password">
            <p class = "msg">{{ $t("g5.Confirm your password") }}</p>
            <input class = "input-box" type="text" v-model="confirmPassword">
            <img alt="" class="line" src="imagesine.png" />
            <button class = "submit" @click="handleSubmit">{{ $t("g5.SUBMIT") }}</button>
        </div>
    </div>
</template>

<script>
    export default {
        name:"resetPassword",
        data() {
            return{
                password: "",
                confirmPassword:"",
                uid: this.$route.query.uid,
                token: this.$route.query.token,
            };
        },
        methods:{
            handleSubmit() {
                this.$axios.post("/account/password/reset/confirm/",{
                    new_password1: this.password,
                    new_password2: this.confirmPassword,
                    uid: this.uid,
                    token: this.token,
                }).then(res => {
                    alert("Congratulation, reset password successfully!",res);
                    this.$router.replace({name: "login"});
                }).catch(err => {
                    alert("Something wrong, please check you input correctly.",err)
                    window.location.reload();
                })
            }
        },
    }
</script>

<style scoped>
.main {
  position: relative;
  height:800px;

}

.background {
  width: 100%;
  height: 800px;
  position: relative;
}
.copyright {
  color: white;
  position: absolute;
  left: 560px;
  bottom: 0px;
  display: center;
  text-align: center;
}
.window {
  background-color: white;
  border: 2px solid black;
  border-radius: 16px;
  padding: 20px 0 18px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 999;
}
.title {
  font-size: 24px;
  font-weight: 700;
  line-height: normal;
  color: black;
  margin-bottom: 39px;
  margin-left: 90px;
}
.line {
  width: 432px;
  margin-bottom: 23px;
}

.line-bottom {
    width: 432px;
    margin-top: 20px;
    margin-bottom: 30px;
}
.msg {
  width: 400px;
  font-size: 16px;
  font-weight: 700;
  line-height: normal;
  color: dimgray;
  margin-bottom: 9px;
  margin-left: 15px;
}
.input-box {
  width: 396px;
  height: 32px;
  background-color: white;
  margin-bottom: 30px;
  margin-left: 15px;
  border-radius: 4px;
  border: 2px solid linen;
}
.submit {
  background: none;
  border: 1px solid black;
  margin-bottom: 18px;
  margin-left: 13px;
  border-radius: 8px;
  padding: 13px 172px;
  font-family: "Arial";
  display: flex;
  align-items: center;
  font-size: 16px;
  font-weight: 400;
  line-height: normal;
}
.submit:hover {
  opacity: .3;
  cursor: pointer;
}
</style>