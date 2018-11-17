$(function () {
    var swiper = new Swiper('.swiper-container', {
        spaceBetween: 30,
        centeredSlides: true,
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
    let IMG_BASE_URL = "http://112.74.32.121:8000/";
    $.get('http://127.0.0.1:8000/Movies/', function (result) {
        if (result.status === 200) {
            let $hot_ul = $('.tab_hot');
            let $will_ul = $('.tab_will');
            add_hot($hot_ul);
            add_will($will_ul);
        }

        function add_hot(hot_ul) {
            let movs = result.data;
            for (let a = 5; a < 10; a++) {
                hot_ul
                    .append(
                        $('<li>')
                            .append(
                                $('<div>')
                                    .addClass('movies')
                                    .append(
                                        $('<img>').attr("src", IMG_BASE_URL + movs[a].image)
                                    )
                                    .append(
                                        $('<p>').addClass('clear').text(movs[a].name)
                                    )
                                .append(
                                    $('<div>').addClass('movies_desc')
                                        .append($('<p>').text("主演:" + movs[a].actor))
                                        .append($('<p>').text("类别:" + movs[a].type_name))
                                        .append($('<p>').text("地区:" + movs[a].loc_name))
                                )
                            )
                            .append($('<button class="buy">选座购票</button>')
                            )
                    )
            }
            show_tab_content($('.movies'), '.movies_desc')
        }

        function add_will(will_ul) {
            let mov = result.data;
            for (let i = 0; i < 5; i++) {
                will_ul
                    .append(
                        $('<li>')
                            .append(
                                $('<div>')
                                    .addClass('movies')
                                    .append(
                                        $('<img>').attr("src", IMG_BASE_URL + mov[i].image)
                                    )
                                    .append(
                                        $('<p>').addClass('clear').text(mov[i].name)
                                    )
                                .append(
                                    $('<div>').addClass('movies_desc')
                                        .append($('<p>').text("主演:" + mov[a].actor))
                                        .append($('<p>').text("类别:" + mov[a].type_name))
                                        .append($('<p>').text("地区:" + mov[a].loc_name))
                                )
                            )
                            .append($('<p>').text("上映时间:" + mov[i].on_decade).addClass('will_p')
                            )
                    )
            }
            show_tab_content($('.movies'), '.movies_desc')
        }

        $('.hot_btn').click(function () {
            $(this).addClass('tab_checked');
            $('.will_btn').removeClass('tab_checked');
            $('.tab_hot').show();
            $('.tab_will').hide();
        });
        $('.will_btn').click(function () {
            $(this).addClass('tab_checked');
            $('.hot_btn').removeClass('tab_checked');
            $('.tab_hot').hide();
            $('.tab_will').show();
        })
    });
});

function show_tab_content(movies, movies_desc) {
    movies.mouseover(function () {
        //设置电影简介部分显示
        $(this).find(movies_desc).slideDown('fast')
    });

    movies.mouseleave(function () {
        //设置电影简介部分隐藏
        $(this).find(movies_desc).slideUp('fast')
    });
}

