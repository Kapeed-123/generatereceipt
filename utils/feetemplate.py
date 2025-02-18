# Write some template
def feetemplate():
    """"
    creating html template with variable
    """

    template = """<html>
                <body style="background-color:#e2e1e0;
                font-family: Open Sans, sans-serif;font-size:100%;
                font-weight:400;line-height:1.4;color:#000;">
                <table style="max-width:670px;margin:50px auto 10px;
                background-color:#fff;padding:50px;-webkit-border-radius:3px;
                -moz-border-radius:3px;border-radius:3px;
                -webkit-box-shadow:0 1px 3px rgba(0,0,0,.12),
                0 1px 2px rgba(0,0,0,.24);-moz-box-shadow:0 1px 3px
                  rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.24);
                  box-shadow:0 1px 3px rgba(0,0,0,.12),0 1px
                  2px rgba(0,0,0,.24);
                  border-top: solid 10px green;">
                    <thead>
                    <tr>
                        <th style="text-align:left;">
                            <img style="max-width: 40px;"
                             src="../images/2452184.png"
                             alt="learningdhara.com" />
                            <a href="https://www.learningdhara.com/">
                            learningdhara.com</a>
                            <p style="font-size:9px;">
                            <span style="font-weight:bold;">
                            (Community towards new technology learning)</span>
                            </p>
                            </th>
                        <th style="text-align:right;font-weight:400;">
                        {receiptdate}</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td style="height:35px;"></td>
                    </tr>
                    <tr>
                        <td colspan="2" style="border: solid 1px #ddd;
                        padding:10px 20px;">
                        <p style="font-size:14px;margin:0 0 6px 0;">
                        <span style="font-weight:bold;display:inline-block;
                        min-width:150px">Fee status</span>
                        <b style="color:green;font-weight:normal;margin:0">
                        {status}</b></p>
                        <p style="font-size:14px;margin:0 0 6px 0;">
                        <span style="font-weight:bold;display:inline-block;
                        min-width:146px">Transaction ID</span>
                        {transactionid}</p>
                        <p style="font-size:14px;margin:0 0 0 0;">
                        <span style="font-weight:bold;display:inline-block;
                        min-width:146px">Fee amount</span>
                        Rs. {amount}</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="height:35px;"></td>
                    </tr>
                    <tr>
                        <td style="width:50%;padding:20px;vertical-align:top">
                        <p style="margin:0 0 10px 0;padding:0;font-size:14px;">
                        <span style="display:block;font-weight:bold;
                        font-size:13px">Name</span>
                         {name}</p>
                        <p style="margin:0 0 10px 0;padding:0;font-size:14px;">
                        <span style="display:block;font-weight:bold;
                        font-size:13px;">Email</span> {email}</p>
                        <p style="margin:0 0 10px 0;padding:0;font-size:14px;">
                        <span style="display:block;font-weight:bold;
                        font-size:13px;">Phone</span> {phone}</p>
                        <p style="margin:0 0 10px 0;padding:0;font-size:14px;">
                        <span style="display:block;font-weight:bold;
                        font-size:13px;">ID No.</span> {accountid}</p>
                        </td>
                        <td style="width:50%;padding:20px;vertical-align:top">
                        <p style="margin:0 0 10px 0;padding:0;font-size:14px;">
                        <span style="display:block;font-weight:bold;
                        font-size:13px;">Bundle Subscription</span>
                        Python, Spark, AWS, GCP, ML, AI</p>
                        <p style="margin:0 0 10px 0;padding:0;font-size:14px;">
                        <span style="display:block;font-weight:bold;
                        font-size:13px;">Class Category</span> {classcat}</p>
                        <p style="margin:0 0 10px 0;padding:0;font-size:14px;">
                        <span style="display:block;font-weight:bold;
                        font-size:13px;">Duration of learning</span>
                        {startdate} to {enddate}</p>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2" style="font-size:14px;
                        padding:50px 15px 0 15px;">
                        <span style="display:block;margin:0 0 10px 0;">
                        {digitalsign}</span>
                        <strong style="display:block;margin:0 0 10px 0;">
                        Signature</strong>
                        </td>
                    </tr>
                    </tfooter>
                </table>
                </body>
                </html>
                """

    return template
