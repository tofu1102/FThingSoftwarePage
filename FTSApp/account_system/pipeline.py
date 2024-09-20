from social_core.exceptions import AuthForbidden

def save_line_profile(backend, user, response, *args, **kwargs):
    """
    LINEのプロフィール情報を取得し、ユーザーモデルに保存する
    """
    if backend.name == 'line':
        print(response)
        # LINEから取得したデータ
        line_user_id = response.get('userId')  # LINEのユーザーID
        line_display_name = response.get('displayName')  # 表示名
        line_picture_url = response.get('pictureUrl')  # プロフィール画像のURL

        # ユーザーオブジェクトのフィールドにデータを保存
        if line_user_id:
            user.line_user_id = line_user_id
            user.line_authorized = True
        if line_display_name:
            user.line_display_name = line_display_name
            user.username = line_display_name
        if line_picture_url:
            user.line_picture_url = line_picture_url

        user.save()

    return {'user': user}

