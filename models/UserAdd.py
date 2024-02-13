import datetime


class UserAdd:
    def __init__(
        self,
        Password=None,
        PasswordInvestor=None,
        Login=None,
        Group=None,
        CertSerialNumber=None,
        Rights=None,
        Registration=None,
        LastAccess=None,
        Name=None,
        Company=None,
        Account=None,
        Country=None,
        Language=None,
        City=None,
        State=None,
        ZipCode=None,
        Address=None,
        Phone=None,
        EMail=None,
        Id=None,
        Status=None,
        Comment=None,
        Color=None,
        PhonePassword=None,
        Leverage=None,
        Agent=None,
        Balance=None,
        Credit=None,
        InterestRate=None,
        CommissionDaily=None,
        CommissionMonthly=None,
        CommissionAgentDaily=None,
        CommissionAgentMonthly=None,
        BalancePrevDay=None,
        BalancePrevMonth=None,
        EquityPrevDay=None,
        EquityPrevMonth=None,
        LastPassChange=None,
        Mqid=None,
        LeadCampaign=None,
        LeadSource=None,
        ClientID=None,
        FirstName=None,
        LastName=None,
        MiddleName=None,
        OtpSecret=None,
    ):

        self.Password: str = Password
        self.PasswordInvestor: str = PasswordInvestor
        self.Login: int = Login
        self.Group: str = Group
        self.CertSerialNumber: int = CertSerialNumber
        self.Rights: str = Rights
        self.Registration: datetime = Registration
        self.LastAccess: datetime = LastAccess
        self.Name: str = Name
        self.Company: str = Company
        self.Account: str = Account
        self.Country: str = Country
        self.Language: int = Language
        self.City: str = City
        self.State: str = State
        self.ZipCode: str = ZipCode
        self.Address: str = Address
        self.Phone: str = Phone
        self.EMail: str = EMail
        self.Id: str = Id
        self.Status: str = Status
        self.Comment: str = Comment
        self.Color: int = Color
        self.PhonePassword: str = PhonePassword
        self.Leverage: int = Leverage
        self.Agent: int = Agent
        self.Balance: float = Balance
        self.Credit: int = Credit
        self.InterestRate: int = InterestRate
        self.CommissionDaily: int = CommissionDaily
        self.CommissionMonthly: int = CommissionMonthly
        self.CommissionAgentDaily: int = CommissionAgentDaily
        self.CommissionAgentMonthly: int = CommissionAgentMonthly
        self.BalancePrevDay: int = BalancePrevDay
        self.BalancePrevMonth: int = BalancePrevMonth
        self.EquityPrevDay: int = EquityPrevDay
        self.EquityPrevMonth: int = EquityPrevMonth
        self.LastPassChange: datetime = LastPassChange
        self.Mqid: str = Mqid
        self.LeadCampaign: str = LeadCampaign
        self.LeadSource: str = LeadSource
        self.ClientID: int = ClientID
        self.FirstName: str = FirstName
        self.LastName: str = LastName
        self.MiddleName: str = MiddleName
        self.OtpSecret: str = OtpSecret

    def __json__(self):
        return {
            "Password": self.Password,
            "PasswordInvestor": self.PasswordInvestor,
            "Login": self.Login,
            "Group": self.Group,
            "CertSerialNumber": self.CertSerialNumber,
            "Rights": self.Rights,
            "Registration": self.Registration,
            "LastAccess": self.LastAccess,
            "Name": self.Name,
            "Company": self.Company,
            "Account": self.Account,
            "Country": self.Country,
            "Language": self.Language,
            "City": self.City,
            "State": self.State,
            "ZipCode": self.ZipCode,
            "Address": self.Address,
            "Phone": self.Phone,
            "EMail": self.EMail,
            "Id": self.Id,
            "Status": self.Status,
            "Comment": self.Comment,
            "Color": self.Color,
            "PhonePassword": self.PhonePassword,
            "Leverage": self.Leverage,
            "Agent": self.Agent,
            "Balance": self.Balance,
            "Credit": self.Credit,
            "InterestRate": self.InterestRate,
            "CommissionDaily": self.CommissionDaily,
            "CommissionMonthly": self.CommissionMonthly,
            "CommissionAgentDaily": self.CommissionAgentDaily,
            "CommissionAgentMonthly": self.CommissionAgentMonthly,
            "BalancePrevDay": self.BalancePrevDay,
            "BalancePrevMonth": self.BalancePrevMonth,
            "EquityPrevDay": self.EquityPrevDay,
            "EquityPrevMonth": self.EquityPrevMonth,
            "LastPassChange": self.LastPassChange,
            "Mqid": self.Mqid,
            "LeadCampaign": self.LeadCampaign,
            "LeadSource": self.LeadSource,
            "ClientID": self.ClientID,
            "FirstName": self.FirstName,
            "LastName": self.LastName,
            "MiddleName": self.MiddleName,
            "OtpSecret=": self.OtpSecret,
        }
