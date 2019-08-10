$(function () {
    //获取backtype属性
    var back_type = $('.thisli').attr('back_type');
    var page = 1;
    var num = 0;//总个数
    var next = 1;
    var tag = 1; //请求状态

    //发送请求
    function get_info() {


        if (next && tag) {
            tag = 0;
            $.ajax({
                url: `/ajax_feedback/?back_type=${back_type}&page=${page}`,
                success: function (res) {
                    // console.log(res);
                    var results = res.results;    //img数据的列表
                    // console.log(result[0].img);  //获取到img的路径
                    next = res.next;

                    for (var i in results) {
                        var row = results[i];
                        var col = $('.column')[num % 4];


                        var item = `<div class="item">
                            <div class="animate-box">
                                <a href="${row.img}"
                                   class="image-popup fh5co-board-img"><img
                                        src="${row.img} "
                                        alt="Free HTML5 Bootstrap template"></a>
                            </div>
                        </div>`;
                        $(col).append(item);

                        //解决加载图片白色问题
                        ;(function () {

                            'use strict';

                            // iPad and iPod detection
                            var isiPad = function () {
                                return (navigator.platform.indexOf("iPad") != -1);
                            };

                            var isiPhone = function () {
                                return (
                                    (navigator.platform.indexOf("iPhone") != -1) ||
                                    (navigator.platform.indexOf("iPod") != -1)
                                );
                            };

                            // OffCanvass
                            var offCanvass = function () {
                                $('body').on('click', '.js-fh5co-menu-btn, .js-fh5co-offcanvass-close', function () {
                                    $('#fh5co-offcanvass').toggleClass('fh5co-awake');
                                });
                            };

                            // Click outside of offcanvass
                            var mobileMenuOutsideClick = function () {
                                $(document).click(function (e) {
                                    var container = $("#fh5co-offcanvass, .js-fh5co-menu-btn");
                                    if (!container.is(e.target) && container.has(e.target).length === 0) {
                                        if ($('#fh5co-offcanvass').hasClass('fh5co-awake')) {
                                            $('#fh5co-offcanvass').removeClass('fh5co-awake');
                                        }
                                    }
                                });

                                $(window).scroll(function () {
                                    if ($(window).scrollTop() > 500) {
                                        if ($('#fh5co-offcanvass').hasClass('fh5co-awake')) {
                                            $('#fh5co-offcanvass').removeClass('fh5co-awake');
                                        }
                                    }
                                });
                            };

                            // Magnific Popup
                            var magnifPopup = function () {
                                $('.image-popup').magnificPopup({
                                    type: 'image',
                                    removalDelay: 300,
                                    mainClass: 'mfp-with-zoom',
                                    titleSrc: 'title',
                                    gallery: {
                                        enabled: true
                                    },
                                    zoom: {
                                        enabled: true, // By default it's false, so don't forget to enable it
                                        duration: 300, // duration of the effect, in milliseconds
                                        easing: 'ease-in-out', // CSS transition easing function
                                        // The "opener" function should return the element from which popup will be zoomed in
                                        // and to which popup will be scaled down
                                        // By defailt it looks for an image tag:
                                        opener: function (openerElement) {
                                            // openerElement is the element on which popup was initialized, in this case its <a> tag
                                            // you don't need to add "opener" option if this code matches your needs, it's defailt one.
                                            return openerElement.is('img') ? openerElement : openerElement.find('img');
                                        }
                                    }
                                });
                            };
                            var animateBoxWayPoint = function () {

                                if ($('.animate-box').length > 0) {
                                    $('.animate-box').waypoint(function (direction) {
                                        if (direction === 'down' && !$(this).hasClass('animated')) {
                                            $(this.element).stop().animate({
                                                opacity: 1
                                            })
                                        }
                                    }, {offset: '75%'});
                                }
                            };

                            $(function () {
                                magnifPopup();

                                animateBoxWayPoint();
                            });

                        }());
                        num += 1;
                    }
                    page += 1;
                    tag = 1;
                },
                // error: function () {
                //     tag = 0;
                // }
            })
        }

    }


    get_info();
    //同学说分批加载
    $(window).scroll(function () {
        //$(document).scrollTop() 滚动条位置距页面顶部的距离；
        //$(document).height() 整个页面的总高度；
        //$(window).height() 当前窗口的高度；

        //判断是否已经滚动到页面底部；
        if ($(document).scrollTop() >= $(document).height() - $(window).height() - 180) {
            get_info();
            // alert(1)
        }
        // alert(1111)
    });


}());