from django.urls import path
from . import views

#URLパターンの逆引き
app_name = 'edu'

#URLパターンを登録するための変数
urlpatterns = [
    #eduアプリへのアクセスは、viewモジュールのIndexViewにリダイレクト
    path('', views.IndexView.as_view(), name='index'),

    # 学習情報投稿ページへのアクセスはviewsモジュールのCreateEduViewを実行
    path('post/', views.CreateEduView.as_view(), name='post'),

    # 職業別学習情報投稿ページへのアクセスはviewsモジュールのCreateJobEduViewを実行
    path('post_job/', views.CreateJobEduView.as_view(), name='post_job'),

    # 投稿完了ページへのアクセスは、viewsモジュールのPostSuccessViewを実行
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),

    # 講座情報カテゴリ一覧ページ
    # cat/<CategoryテーブルのID値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('cat/<int:category>', views.CategoryView.as_view(), name='cat'),

    # 講座情報詳細ページ
    # post-detail/<edu postsテーブルのid値>にマッチング
    # <int:pk>は、辞書{pk: id値}として、DeitalViewに渡される。
    path('post_detail/<int:pk>', views.DetailView.as_view(), name='post_detail'),

    # eduアプリ内のモデル化した職業情報へのアクセスは、viewモジュールのModelIndexViewにリダイレクト
    path('m/', views.ModelIndexView.as_view(), name='model_index'),

    # 専門分野一覧ページ
    # line/<LineテーブルのID値>にマッチング
    # <int:line>は辞書{line: id値(int)}としてLineViewに渡される
    path('line/<int:line>', views.LineView.as_view(), name='line'),

    # 職業モデル詳細ページ
    # model-detail/<JobPostsテーブルのid値>にマッチング
    # <int:pk>は、辞書{pk: id値}として、ModelDeitalViewに渡される。
    path('model_detail/<int:pk>', views.ModelDetailView.as_view(), name='model_detail'),

    # 学習情報のマイページ
    # mypage_edu/へのアクセスに、MypageEduView実行
    path('mypage_edu/', views.MypageEduView.as_view(), name='mypage_edu'),

    # 学習情報のマイページ
    # mypage_job/へのアクセスに、MypageJobView実行
    path('mypage_job/', views.MypageJobView.as_view(), name='mypage_job'),

    # 学習情報の投稿削除
    # post_detail/学習情報のテーブルID/delete にマッチング
    path('post_detail/<int:pk>/delete', views.EduPostDeleteView.as_view(), name='post_delete'),

    # 職種別学習情報の投稿削除
    # model_detail/職種別学習情報のテーブルID/delete にマッチング
    path('model_detail/<int:pk>/delete', views.JobPostDeleteView.as_view(), name='model_delete'),
]
