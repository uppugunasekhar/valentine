from django.shortcuts import render, get_object_or_404, render_to_response 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from valentine.models import UserEntry,EntryChoice
from django.utils import timezone
import datetime
import urllib2
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, BadHeaderError
from django.template.context import RequestContext
from ipware.ip import get_ip
import ipdb
from facepy import GraphAPI
from django_facebook.decorators import facebook_required
from facepy.exceptions import OAuthError
#from facepy.utils import get_extended_access_token
from social_auth.models import UserSocialAuth


def index(request):
		context = RequestContext(request,{'request': request,'user': request.user})
		return render_to_response('valentine/index.html',context_instance=context)

def middle(request):
	try:
		instance = UserSocialAuth.objects.filter(provider='facebook').get(id = request.user.id-1)
		graph = GraphAPI(instance.extra_data['access_token'])
		#graph.post(
				#path = 'me/feed',
				#message = 'use this awesome app valentine',
				#link='http://valentine.com:8000'
				#) 
		profile_pic=graph.get(
				path = 'me/picture?fields = url&redirect=false&height=150&width=150',
				) 
		context = RequestContext(request,{'request': request,'user': request.user, 'profile_pic':profile_pic})
		return render_to_response('valentine/sub1.html',context_instance = context)
	except:
		return HttpResponseRedirect('/')

def register(request):
		if request.method=="POST":
			instance = UserSocialAuth.objects.filter(provider='facebook').get(id = request.user.id-1)
			#short_lived_access_token = 'CAAMkkm5SZCZBcBAE4Rh0ZAhBTetqpxXp6HgRT1ZBcwZCjvvVBgJEHvVWNAZCDLepm92NkyTHcBqlnQuS1RYILzXMvGeVr9haZAy8z5U5xuxJZAklF58dfY5r43ZCIZBMR10xbKoXJiqMpRNMRI1ZCDCX7WD6NDFH1ISChae4JA3AZAUZC9uhxRAQ8aAx1koeaSv27h2Wn90ZAfhZCX3yhjETIs0lNwE'
			#application_id='884636264890343'
			#application_secret_key='76ea9acba9eec25eb8d78ddc57dc1cf3'
			#long_lived_access_token, expires_at = get_extended_access_token(short_lived_access_token, application_id, application_secret_key)
			graph = GraphAPI(instance.extra_data['access_token'])
			
			profile_pic=graph.get(
				path = 'me/picture?fields = url&redirect=false&height=150&width=150',
				) 
			gender = graph.get(
				path = 'me?fields= gender'
				)
			friends=graph.get(
				path='me/friends?fields=friends'
				)
			ip = get_ip(request)
			fbid0=request.user.username
			mailid0=request.POST.get('mailid0',None)
			if mailid0 is None:
				mailid0=request.user.email
			#gender= request.user.gender
			#mailid10=request.POST.get('mailid10',None)
			#place=request.POST.get('place','')
			date_selection=timezone.now()
			try:
				obj_Userentry=UserEntry(user_fullname=fbid0,user_email=mailid0,date_of_selection=date_selection,ip_address=ip)
				obj_Userentry.save()
			except:
				return render_to_response('valentine/error.html',{'user': request.user, 'profile_pic':profile_pic})
			i=1
			namess=[]
			mailids=[]
			altmailids=[]
			while i<6:
				
				names=request.POST.get('name'+str(i),None)				
				mail = request.POST.get('mailid'+str(i),None)
				altmail = request.POST.get('mailid1'+str(i),None)
				obj_Entrychoice=EntryChoice(choice=obj_Userentry)
				if names is not None:
					namess.append(names)
					obj_Entrychoice.choice_names=names
				
				if mail is not None:
					mailids.append(mail)
					obj_Entrychoice.choice_email=mail

				if altmail is not None:
					altmailids.append(altmail)
					obj_Entrychoice.choice_altemail=altmail
				obj_Entrychoice.save()
				i=i+1
			instance = UserSocialAuth.objects.filter(provider='facebook').get(id = request.user.id-1)
			#short_lived_access_token = 'CAAMkkm5SZCZBcBAE4Rh0ZAhBTetqpxXp6HgRT1ZBcwZCjvvVBgJEHvVWNAZCDLepm92NkyTHcBqlnQuS1RYILzXMvGeVr9haZAy8z5U5xuxJZAklF58dfY5r43ZCIZBMR10xbKoXJiqMpRNMRI1ZCDCX7WD6NDFH1ISChae4JA3AZAUZC9uhxRAQ8aAx1koeaSv27h2Wn90ZAfhZCX3yhjETIs0lNwE'
			#application_id='884636264890343'
			#application_secret_key='76ea9acba9eec25eb8d78ddc57dc1cf3'
			#long_lived_access_token, expires_at = get_extended_access_token(short_lived_access_token, application_id, application_secret_key)
			graph = GraphAPI(instance.extra_data['access_token'])
			
			profile_pic=graph.get(
				path = 'me/picture?fields = url&redirect=false&width=150&height=150',
				) 
			gender = graph.get(
				path = 'me?fields= gender'
				)
			friends=graph.get(
				path='me/friends?fields=friends'
				)
			profile_picc=profile_pic['data']
			#obj_Userentry.user_pic = profile_picc['url']
			#friends_countt=friends['summary']
			#obj_Userentry.friends_count=friends_countt['total_count']
			obj_Userentry.gender = gender['gender']
			obj_Userentry.save() 
			#send_mail(subject,flag,'sampleimaginate@gmail.com',[mailid0,mailid10])	
			trymail='Heyyy...!! Here is an awesome way to express your feelings on your secret crush without disclosing your identity. Some of your friends made a try and conveyed their crush on you. You are just a click away ( http://coffeehangout.com) from finding your secret crush... '	
			matchflag='It seems like your crush is yet to convey her feelings. We have sent her a mail anonymously. Just stay calm and keep Loving your Crush...!! We will notify you when your crush responds'
			subject='valentine app results'
			for mail in mailids:
				if mail is not None:
					try:
						send_mail(subject,trymail,'cupid@coffeehangout.com',[mail])
					except:
						mail=None

			for mail in altmailids:
				if mail is not None:
					try:
						send_mail(subject,trymail,'cupid@coffeehangout.com',[mail])
					except:
						mail=None
			if UserEntry.objects.all()>1:
				for i in range(0,5):
					#choice_fb_obj = UserEntry.objects.filter(user_fb = fbids[i],match_email=None)
					choice_email_obj = UserEntry.objects.filter(user_email = mailids[i],match_email=None)
					#choice_emailaltemail_obj = UserEntry.objects.filter(user_altemail = mailids[i],match_email=None,friends_count__gt=40)
					choice_altemailemail_obj = UserEntry.objects.filter(user_email = altmailids[i],match_email=None)
						#choice_altemail_obj = UserEntry.objects.filter(user_altemail = altmailids[i],match_email=None,friends_count__gt=40)
					#choicesfb = EntryChoice.objects.all().filter(choice = choice_fb_obj)
					choicesemail = EntryChoice.objects.all().filter(choice = choice_email_obj)
					#choicesemailaltemail = EntryChoice.objects.all().filter(choice = choice_emailaltemail_obj)
					choicesaltemailemail = EntryChoice.objects.all().filter(choice = choice_altemailemail_obj)
					#choicesaltemail = EntryChoice.objects.all().filter(choice = choice_altemail_obj)
					flag = 'unmatch'
						
					if flag =='unmatch':
						for matchemail in choicesemail:
							if matchemail.choice_email==mailid0:
								flag='match'
								obj_Userentry.match_email=mailids[i]
								obj_Userentry.save()
								obj_Userentry.date_of_match=timezone.now()
								obj_Userentry.save()
								choice_email_match = UserEntry.objects.get(user_email = mailids[i])
								choice_email_match.match_email=mailid0
								choice_email_match.date_of_match=timezone.now()
								choice_email_match.save()
								matchflag= 'Congrats...!! Your crush already expressed feelings on you and waiting for you... Go and have a lovely hangout with your crush,%s @ %s'%(namess[i],mailids[i])
								matchflag1='Yippie..!! And now the wait is over... Your crush, %s responded on having a secret crush on you. Go and have a lovely hangout with your crush, @ %s'%(fbid0,mailid0)
								send_mail(subject,matchflag1,'cupid@coffeehangout.com',[mailids[i]])
								break
							
							elif matchemail.choice_altemail==mailid0:
								flag='match'
								obj_Userentry.match_email=mailids[i]
								obj_Userentry.save()
								obj_Userentry.date_of_match=timezone.now()
								obj_Userentry.save()
								choice_email_match = UserEntry.objects.get(user_email = mailids[i])
								choice_email_match.match_email=mailid0
								choice_email_match.date_of_match=timezone.now()
								choice_email_match.save()
								matchflag='Congrats...!! Your crush already expressed feelings on you and waiting for you... Go and have a lovely hangout with your crush,%s @ %s'%(namess[i],mailids[i])

								matchflag1='Yippie..!! And now the wait is over... Your crush, %s responded on having a secret crush on you. Go and have a lovely hangout with your crush, @ %s'%(fbid0,mailid0)
								send_mail(subject,matchflag1,'cupid@coffeehangoutcom',[mailids[i]])
								break

								

						

					if flag =='unmatch':
						for matchemail in choicesaltemailemail:
							if matchemail.choice_email==mailid0:
								flag='match'
								obj_Userentry.match_email=altmailids[i]
								obj_Userentry.save()
								obj_Userentry.date_of_match=timezone.now()
								obj_Userentry.save()
								choice_email_match = UserEntry.objects.get(user_email = altmailids[i])
								choice_email_match.match_email=mailid0
								choice_email_match.date_of_match=timezone.now()
								choice_email_match.save()
								matchflag='Congrats...!! Your crush already expressed feelings on you and waiting for you... Go and have a lovely hangout with your crush,%s @ %s'%(namess[i],altmailids[i])

								matchflag1='Yippie..!! And now the wait is over... Your crush, %s responded on having a secret crush on you. Go and have a lovely hangout with your crush, @ %s'%(fbid0,mailid0)
								send_mail(subject,matchflag1,'cupid@coffeehangout.com',[altmailids[i]])
								break
							elif matchemail.choice_altemail==mailid0:
								flag='match'
								obj_Userentry.match_email=altmailids[i]
								obj_Userentry.save()
								obj_Userentry.date_of_match=timezone.now()
								obj_Userentry.save()
								choice_email_match = UserEntry.objects.get(user_email = altmailids[i])
								choice_email_match.match_email=mailid0
								choice_email_match.date_of_match=timezone.now()
								choice_email_match.save()
								matchflag='Congrats...!! Your crush already expressed feelings on you and waiting for you... Go and have a lovely hangout with your crush,%s @ %s'%(namess[i],altmailids[i])

								matchflag1='Yippie..!! And now the wait is over... Your crush, %s responded on having a secret crush on you. Go and have a lovely hangout with your crush, @ %s'%(fbid0,mailid0)
								send_mail(subject,matchflag1,'cupid@coffeehangout.com',[altmailids[i]])
								break

					if flag is 'match':
						send_mail(subject,matchflag,'cupid@coffeehangout.com',[mailid0])
						return render(request, 'valentine/success.html', {'matchflag': matchflag,'user': request.user, 'profile_pic':profile_pic} )
			
			send_mail(subject,matchflag,'cupid@coffeehangout.com',[mailid0])
			return render(request, 'valentine/success.html', {'matchflag': matchflag,'user': request.user, 'profile_pic':profile_pic} )
			
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')			
		
		
		
		





		
