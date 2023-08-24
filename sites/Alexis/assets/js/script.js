burgermenu.onclick = function myFunction1(){
    var x = document.getElementById("mytopnav");

    if (x.className ==="menu"){
        x.className +="-responsive";
    } else{
        x.className = "menu";
    }

}

var link = document.getElementById("myLink");
var div = document.getElementById("myDiv");
var video = document.getElementById("myVideo");

link.addEventListener("click", function(event) {
    event.preventDefault();
    
    if (div.style.display === "none") {
        div.style.display = "flex";
        
        video.pause();
        video.currentTime = 0;
    } else {
        div.style.display = "none";
        
        video.play();
    }
});

video.addEventListener("ended", function() {
    div.style.display = "flex";
});

video.addEventListener("pause", function() {
    div.style.display = "flex";
});


const textElement = document.getElementById('commentar');
const nameElement = document.getElementById('name');
const profile1 = document.querySelectorAll('.profile1');
const profile2 = document.querySelectorAll('.profile2');
const profile3 = document.querySelectorAll('.profile3');
const profile4 = document.querySelectorAll('.profile4');
const borderElement = document.getElementById('team-com');
const colors = ['#FC5F45', '#38C695', '#B27CF5', '#FEB960'];

var dict = {
    "Michael Schmitt": "In my role as a Founder & SEO specialist, I find immense satisfaction and purpose. Being a founder allows me to shape the company's vision, drive innovation, and foster a dynamic work environment. Witnessing the growth and success of the company as a result of collective efforts is truly fulfilling. As an SEO specialist, I'm passionate about deciphering the intricacies of search algorithms and crafting strategies that propel our online presence. I firmly believe that organic growth is the cornerstone of sustainable success in the digital era. Seeing our website climb the ranks and connect with a wider audience validates the impact of our efforts.",
    "Dawid Kramer": "As a lead developer, I aspire for our code to be not only efficient but also elegant. I believe in the importance of continuous learning and open knowledge sharing with colleagues. I consider interaction and collaboration within the team to be key factors in achieving outstanding results. My goal is to not only create products but also inspire other team members to strive for excellence. The development process, for me, is not just a routine task; it's a creative approach to solving complex problems and enhancing user experiences.",
    "Anna Schroder": "Interacting with other team members helps me better understand the needs and goals of the project. I am confident that good design starts with thorough analysis and discussion, ultimately leading to creative solutions that align with our objectives. The design process is a constant journey of exploration and refinement. I believe that design holds the power to not only enhance the product's aesthetics but also to create emotional and functional interactions. My work is my passion, and I take pride in the opportunity to make a significant contribution to the success and visual perception of our projects.",
    "Jason Teichmann": "As a consultant, I derive immense satisfaction from the opportunity to provide meaningful support and influence. My goal is to assist clients in achieving their business objectives by offering expert knowledge and a strategic perspective on issues. Each project presents a new challenge that demands deep analysis and innovative approaches. Collaborating with clients fosters mutual learning and growth. Relationships built on trust and partnership create a productive platform for achieving shared goals. My role as a consultant entails continuous development and a drive to impact the success of businesses. I take pride in being a resource for clients, providing them with necessary insights and helping them effectively tackle challenges and realize their strategic ambitions."
}

profile1.forEach((block) => {
    block.addEventListener('mouseenter', () => {
        nameElement.textContent = `Michael Schmitt`;
        textElement.textContent = `${dict["Michael Schmitt"]}`;
        borderElement.style.border = "3px solid #FC5F45";
        const linkElements = document.querySelectorAll('.original');
        linkElements.forEach((linkElement) => {
            linkElement.addEventListener('mouseenter', () => {
                linkElement.style.color = colors[0];
            });

            linkElement.addEventListener('mouseleave', () => {
                linkElement.style.color = '#616161';
            });
        });
        
    });
});

profile2.forEach((block) => {
    block.addEventListener('mouseenter', () => {
        nameElement.textContent = `Dawid Kramer`;
        textElement.textContent = `${dict["Dawid Kramer"]}`;
        borderElement.style.border = "3px solid #38C695"; 
        const linkElements = document.querySelectorAll('.original');
        linkElements.forEach((linkElement) => {
            linkElement.addEventListener('mouseenter', () => {
                linkElement.style.color = colors[1];
            });

            linkElement.addEventListener('mouseleave', () => {
                linkElement.style.color = '#616161';
            });
        });
        
    });
});

profile3.forEach((block) => {
    block.addEventListener('mouseenter', () => {
        nameElement.textContent = `Anna Schroder`;
        textElement.textContent = `${dict["Anna Schroder"]}`;
        borderElement.style.border = "3px solid #B27CF5";
        const linkElements = document.querySelectorAll('.original');
        linkElements.forEach((linkElement) => {
            linkElement.addEventListener('mouseenter', () => {
                linkElement.style.color = colors[2];
            });

            linkElement.addEventListener('mouseleave', () => {
                linkElement.style.color = '#616161';
            });
        });
        
    });
});

profile4.forEach((block) => {
    block.addEventListener('mouseenter', () => {
        nameElement.textContent = `Jason Teichmann`;
        textElement.textContent = `${dict["Jason Teichmann"]}`;
        borderElement.style.border = "3px solid #FEB960";
        const linkElements = document.querySelectorAll('.original');
        linkElements.forEach((linkElement) => {
            linkElement.addEventListener('mouseenter', () => {
                linkElement.style.color = colors[3];
            });

            linkElement.addEventListener('mouseleave', () => {
                linkElement.style.color = '#616161';
            });
        });
        
    });
});

var information = {
    "1": ["Robert Stone is a visionary leader at NexaSynergy, where he holds the role of Chief Innovation Officer. With a background in technology and finance, Robert has orchestrated successful crowdfunding campaigns, harnessing the power of network effects and user experience to drive funding success. His expertise in equity series funding and strategic partnerships has propelled NexaSynergy to new heights, making him a key player in the industry.", "Robert", "Robert Stone", "Chief Innovation Officer, NexaSynergy"],
    "2": ["Eduardo Fernandez is a tech visionary with a strong background in software engineering. He played a crucial role in developing TechFusion's groundbreaking product. His expertise in deploying complex systems and maintaining ownership of the codebase has been instrumental in the company's success. Eduardo's dedication to non-disclosure agreements and ensuring the security of the company's intellectual property is highly valued.", "Eduardo", "Eduardo Fernandez", "Co-Founder & CTO, TechFusion"],
    "3": ["Lena Vasquez is a marketing powerhouse known for her strategic thinking and influencer partnerships. As VP of Marketing at Boostify, she successfully orchestrated a series of equity crowdfunding campaigns that fueled the company's growth. With a focus on user experience and leveraging network effects, Lena has managed to turn Boostify into a crowdfunding rockstar, driving impressive traction and engagement.", "Lena", "Lena Vasquez", "VP of Marketing, Boostify"],
    "4": ["Nikolai Petrov is a financial guru and a master at navigating the intricacies of financing and equity. As the CFO of CapitalWise, he has overseen multiple rounds of funding, employing a mix of strategies like vesting periods and careful analysis of burn rates. His deep understanding of stock options, bootstrapping, and financial modeling has enabled CapitalWise to maintain a strong financial foundation.", "Nikolai", "Nikolai Petrov", "CFO, CapitalWise"],
    "5": ["Ariana Chen is a brilliant mind in product development, driving user-focused innovations at Connectify. Her direct mailing strategies have played a pivotal role in user acquisition, and she has managed to build a creative and high-performing team. Ariana's expertise in crafting seamless user experiences and utilizing crowdsource inputs has made Connectify's product a favorite among users.", "Ariana", "Ariana Chen", "Director of Product Development, Connectify"],
    "6": ["Roberta Nguyen is a dynamic entrepreneur known for her exceptional leadership skills. As the Co-Founder and CEO of LaunchLinx, she has established herself as a master of deployment and project ownership. With a sharp focus on non-disclosure agreements and meticulous attention to detail, Roberta has ensured the security and success of every project her company takes on. Her strategic thinking and commitment to equity have made LaunchLinx a leading player in the industry.", "Roberta", "Roberta Nguyen", "Co-Founder & CEO, LaunchLinx"]
}

function changeText(num) {
    const paragraph = document.getElementById('par-think');
    const podpis = document.getElementById('podpis-think');
    const name = document.getElementById('name-think');
    const location = document.getElementById('loc-think');
    paragraph.textContent = information[num][0];
    podpis.textContent = information[num][1];
    name.textContent = information[num][2];
    location.textContent = information[num][3];

}




$("#sendMail").on("click", function(){
    var user = $("#user").val().trim();
    var subject = $("#subject").val().trim();
    var YourEmail = $("#YourEmail").val().trim();
    var ProjectBudget = $("#ProjectBudget").val().trim();
    var YourMessage = $("#YourMessage").val().trim();

    if ((user == "") || (subject == "") || (YourEmail == "") || (ProjectBudget == "") || (YourMessage == "")){
        $("#errorMess").text("Fill in the fields");
        return false;
    } 

    $("#errorMess").text("");

    $.ajax({
        url:'ajax/mail.php',
        type:'POST',
        cache:false,
        data:{'user':user,'subject':subject,'YourEmail':YourEmail,'ProjectBudget':ProjectBudget,'YourMessage':YourMessage},
        dataType:'html',
        beforeSend: function(){
        $("#sendMail").prop("disabled", true);
        },
        success:function(data){
        if(!data){
            alert("Wiadomość nie została wysłana");
        }
        else{
            alert("Wiadomość wysłana");
            $("#mailForm").trigger("reset");
        }
        $("#sendMail").prop("disabled", false);
        }
    });

});


