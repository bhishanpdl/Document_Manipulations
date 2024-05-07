css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    position: relative; /* Added position relative */
}

.chat-message.user {
    background-color: #2b313e;
}

.chat-message.bot {
    background-color: #475063;
}

.chat-message .avatar {
    width: 20%;
}

.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 90%;
    padding: 0 1rem;
    color: #fff;
}

.small-font {
    font-size:16px !important;
    color: grey !important;
}

.css-pxxe24 {
    visibility: hidden;
}

</style>
'''

bot_template = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://as2.ftcdn.net/v2/jpg/02/38/04/81/1000_F_238048128_OHsRrwAaqeoGCFdpAX6wNgLmGeI0JWFX.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
<div class="chat-message user">
    <div class="avatar">
        <img src="https://as1.ftcdn.net/v2/jpg/01/18/59/38/1000_F_118593824_CAAfUDVnd5ZwlCLFWkzUQMaSyLX7h33j.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>

'''
