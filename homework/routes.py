from flask import jsonify, request


$( 'form' ).on( 'submit' )



# TEST ROUTE
@api.route('/poster', methods=['POST'])
def get_poster():
    """
    [GET] /api/poster
    """
    data = json.loads(request.data.decode('utf-8'))
    u = User.query.filter_by(email=data['user_email']).first()
    # print(u)
    # posts = [p.to_dict() for p in Post.query.all()]
    return jsonify([p.to_dict() for p in  u.posts.all()])
    # return jsonify(posts)
# TEST ROUTE